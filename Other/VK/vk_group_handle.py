import pickle
import vk_api
import os
from tqdm import tqdm
from collections import Counter

login, password = os.environ['VK_LOGIN'], os.environ['VK_PASSWORD']
vk_session = vk_api.VkApi(login, password)

try:
    vk_session.authorization()
except vk_api.AuthorizationError as error_msg:
    print(error_msg)


tools = vk_api.VkTools(vk_session)
"""
    VkTools.get_all позволяет получить все итемы, например со стены или
    получить все диалоги, или сообщения. При использовании get_all
    сокращается количество запросов к API за счет метода execute в 25 раз.
    Например за раз со стены можно получить 100 * 25 = 2500, где
    100 - максимальное количество постов, которое можно получить за один
    запрос.
"""

result = []

wall = tools.get_all('wall.get', 100, {'owner_id': -76552532})
owner_id_counter = Counter()
id_counter = Counter()

for i, wall_item in tqdm(enumerate(wall["items"])):
    post_id = wall_item.get("id", 0)
    owner_id = wall_item.get('owner_id', 0)

    comments_count = wall_item.get("comments", {}).get("count", 0)

    comments = tools.get_all('wall.getComments', 100, {'owner_id': -76552532, 'post_id': post_id, 'count': comments_count}).get("items", [])
    comments_user_ids = [str(comment.get('from_id', 0)) for comment in comments if comment.get('from_id', 0)]

    if owner_id:
        owner_id_counter.update(str(owner_id))
        id_counter.update(str(owner_id))
    if comments_user_ids:
        id_counter.update(comments_user_ids)

    if i % 100 == 0:
        with open("vk_dumped.pickle", "wb") as file:
            pickle.dump(result, file)

print(owner_id_counter)
print(id_counter)