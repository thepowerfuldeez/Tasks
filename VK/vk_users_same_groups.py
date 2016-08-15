from vk_core import Vk
from tqdm import tqdm

vk = Vk()
users = vk.get_all('groups.getMembers', {
    'group_id': 58219172
})['items']

users_at_group = []

for user_id in tqdm(users):
    groups = vk.get_all('groups.get', {
        'user_id': user_id
    })
    if groups:
        if 125004421 and 79138567 and 30666517 and 63731512 and 68662114 in groups.get('items'):
            users_at_group.append(user_id)

result = vk.method('users.get', {
    'user_ids': repr(users_at_group)[1:-1],
    'fields': 'domain, first_name, last_name'
})

for user in result:
    print("{} {} – http://new.vk.com/{}".format(user.get('first_name'), user.get('last_name'), user.get('domain')))