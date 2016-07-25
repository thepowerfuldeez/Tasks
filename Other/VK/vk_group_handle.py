import pickle
import vk_api
import re
import os
from tqdm import tqdm

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
result_board = []

regex = re.compile('\[.+\]')
# wall = tools.get_all('wall.get', 100, {'owner_id': -76552532})
#
# for i in tqdm(range(len(wall["items"]))):
#     wall_item = wall["items"][i]
#
#     post_text = wall_item.get("text", "")
#     post_id = wall_item.get("id", 0)
#     comments_count = wall_item.get("comments", {}).get("count", 0)
#
#     comments = tools.get_all('wall.getComments', 100, {'owner_id': -76552532, 'post_id': post_id, 'count': comments_count}).get("items", [])
#     comments = [re.sub(regex, "", comment.get("text", "")) for comment in comments if comment.get("text", "")]
#
#     result.append([post_text, comments])
#
#     if i % 100 == 0:
#         with open("vk_dumped.pickle", "wb") as file:
#             pickle.dump(result, file)

group_comments = tools.get_all('board.getComments', 100, {'group_id': 76552532, 'topic_id': 31801553})
for comment in group_comments['items']:
    post_text = re.sub(regex, "", comment.get("text", ""))
    print(post_text)
    result_board.append(post_text)
with open("vk_dumped_board.pickle", "wb") as file:
    pickle.dump(result_board, file)