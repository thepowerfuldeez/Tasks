from bs4 import BeautifulSoup as bs
import requests

import vk_api
import os
# from vk-spbu import TableParser


class TableParser:
    """Парсит табличку, по умолчанию с общим конкурсов, МатОбес и без оригиналов аттестатов.
    Powered by admarkov.ru/rating/spbu"""

    MATOBES_TABLE_OK = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_b83a1ed5-8d4b-4ecb-86cb-c81762b25d0e.html&nobvi=on&first=on"
    MATOBES_TABLE_ORIGINALS = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_b83a1ed5-8d4b-4ecb-86cb-c81762b25d0e.html&orig=on&first=on"
    PMI_TABLE_OK = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_2f51dacc-f17a-4c72-b623-2f0525cbb88a.html&nobvi=on&first=on"
    PMI_TABLE_ORIGINALS = "http://admarkov.ru/rating/spbu?link=https%3A%2F%2Fcabinet.spbu.ru%2FLists%2F1k_EntryLists%2Flist_2f51dacc-f17a-4c72-b623-2f0525cbb88a.html&orig=on&first=on"

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
        self.table = [[td.text for td in tr.find_all("td")] for tr in soup.find("tbody").find_all("tr")]
        self.originals = originals
        self.inf = inf

    def get_contest_num(self, name):
        """Находит вас в табличке и возвращает положение"""
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


vk_session = vk_api.VkApi(os.environ["VK_LOGIN"], os.environ["VK_PASSWORD"], app_id=5559651)
vk_session.authorization()

name = "Григорьев Георгий"
vk_session.method("messages.send", {
    'domain': 'thepowerfuldeez',
    'message': "You're {}".format(TableParser("PMI", True).get_contest_num(name))
})