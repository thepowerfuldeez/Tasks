from vk_spbu import *
from copy import copy

vk = Vk()
table_vk_ids = list(filter(lambda x: x, [vk.get_user_from_cr(cr['name'], *cr['bday'])
            for cr in TableParser(originals=True).get_all_names()]))

table_vk_wrote_ids = [user['user_id'] for user in vk.vk_session.method('messages.search', {
    'q': "Привет! Я знаю, что ты поступаешь в СПбГУ на МатОбес 1 приоритетом.  Вероятно, тебе больше нравится математика",
    'count': 100 })['items']]

t1 = set(int(user[-1]) for user in table_vk_ids)
t2 = set(int(id_) for id_ in table_vk_wrote_ids)
print("Написал {} человек, осталось в таблице {}".format(len(t2), len(t1)))

print(t1.difference(t2))