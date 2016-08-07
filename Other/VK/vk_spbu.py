import requests
import os
import vk_api
from bs4 import BeautifulSoup as bs


class TableParser:
    """Парсит табличку, по умолчанию с общим конкурсов, МатОбес и без оригиналов аттестатов"""

    MATOBES_TABLE_OK = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_b83a1ed5-8d4b-4ecb-86cb-c81762b25d0e.html&nobvi=on&first=on"
    MATOBES_TABLE_ORIGINALS = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_b83a1ed5-8d4b-4ecb-86cb-c81762b25d0e.html&orig=on&first=on"
    PMI_TABLE_OK = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_2f51dacc-f17a-4c72-b623-2f0525cbb88a.html&nobvi=on&first=on"
    PMI_TABLE_ORIGINALS = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_2f51dacc-f17a-4c72-b623-2f0525cbb88a.html&orig=on&first=on"
    PMI_PMIPU_TABLE_ORIGINALS = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_97a05ded-f28d-4929-aead-b6dc7cfc9f99.html&orig=on&first=on"

    def __init__(self, type="MATOBES", originals=False, inf=False):
        if type == "MATOBES":
            if originals:
                soup = bs(requests.get(self.MATOBES_TABLE_ORIGINALS).content, "lxml")
            else:
                soup = bs(requests.get(self.MATOBES_TABLE_OK).content, "lxml")
        elif type == "PMI":
            if originals:
                soup = bs(requests.get(self.PMI_TABLE_ORIGINALS).content, "lxml")
            else:
                soup = bs(requests.get(self.PMI_TABLE_OK).content, "lxml")
        else:
            soup = bs(requests.get(self.PMI_PMIPU_TABLE_ORIGINALS).content, "lxml")

        self.table = [[td.text for td in tr.find_all("td")] for tr in soup.find("tbody").find_all("tr")]
        self.originals = originals
        self.inf = inf

    def get_contest_num(self, name):
        for tr in self.table:
            if name in tr[2]:
                return tr[0]
        return None

    def get_all_names(self):
        cr = []
        for tr in self.table:
            if "Григорьев Георгий" in tr[2]:
                return cr
            if self.inf:
                if "Информатика" in tr[-1] or "Информатика" in tr[-2]:
                    if self.originals:
                        if "Да" in tr[12]:
                            cr.append({"name": " ".join(tr[2].split()[:2]), "bday": map(int, tr[3].split("."))})
                    else:
                        if "Нет" in tr[12]:
                            cr.append({"name": " ".join(tr[2].split()[:2]), "bday": map(int, tr[3].split("."))})
            else:
                if "Информатика" not in tr[-1] and "Информатика" not in tr[-2]:
                    if self.originals:
                        if "Да" in tr[12]:
                            cr.append({"name": " ".join(tr[2].split()[:2]), "bday": map(int, tr[3].split("."))})
                    else:
                        if "Нет" in tr[12]:
                            cr.append({"name": " ".join(tr[2].split()[:2]), "bday": map(int, tr[3].split("."))})
        return cr


class Vk:
    def __init__(self):
        vk_session = vk_api.VkApi(os.environ['VK_LOGIN'], os.environ['VK_PASSWORD'], app_id=5559651)
        vk_session.authorization()
        self.vk_session = vk_session

    def get_user_from_cr(self, name, day, month, year):
        # noinspection PyBroadException
        try:
            r = self.vk_session.method('users.search', {
                'q': name,
                'birth_day': day,
                'birth_month': month,
                'birth_year': year,
                'fields': 'domain, city, can_write_private_message',
                'has_photo': 1
            })
            user = r['items'][0]
            if user['can_write_private_message']:  # Если не закрыта ЛС
                name = user.get('first_name') + ' ' + user.get('last_name')
                city = user.get('city').get('title')
                domain = 'http://new.vk.com/' + user.get('domain')
                id = user.get('id')
                return [domain, name, city, id]
        except:
            return None


def print_into(vk, originals, inf, text, file):
    credentials = TableParser(type="PMI_PMPU", originals=originals, inf=inf).get_all_names()
    # print(len(credentials))
    users = []
    # print(file=file)
    # print(text, file=file)
    # print(file=file)
    print()
    print(text)
    print()
    for cr in credentials:
        user = vk.get_user_from_cr(cr['name'], *cr['bday'])
        if user:
            # r = vk.vk_session.method('messages.getHistory', {
            #     'user_id': user[-1]
            # })
            # if not r.get('count', 0):
                users.append(user)
                # print(*user, sep=";", file=file)
                print(*user[:-1], sep='\t')
            # print(len(users))


if __name__ == '__main__':
    vk = Vk()
    with open("spbu-table.csv", "w") as ftable:
        # print(*["VK", "Имя", "Город"], sep=";", file=ftable)
        print(*["VK", "Имя", "Город"], sep="\t")
        print_into(vk, originals=True, inf=True, text="Пред. абитуриенты (Оригинал+Информатика)", file=ftable)
        print_into(vk, originals=True, inf=False, text="Пред. абитуриенты (Оригинал)", file=ftable)
        # print_into(vk, originals=False, inf=True, text="Пред. абитуриенты (ОК+Информатика)", file=ftable)
        # print_into(vk, originals=False, inf=False, text="Пред. абитуриенты (ОК)", file=ftable)
