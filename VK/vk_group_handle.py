import pickle
from tqdm import tqdm
from collections import Counter
from vk_core import Vk

vk = Vk()

wall = vk.get_all('wall.get', {'owner_id': -76552532})
owner_id_counter = Counter()
id_counter = Counter()

for i, wall_item in tqdm(enumerate(wall)):
    post_id = wall_item.get("id", 0)
    owner_id = wall_item.get('owner_id', 0)

    comments_count = wall_item.get("comments", {}).get("count", 0)

    comments = vk.get_all('wall.getComments', {'owner_id': -76552532, 'post_id': post_id, 'count': comments_count})
    comments_user_ids = [str(comment.get('from_id', 0)) for comment in comments if comment.get('from_id', 0)]

    if owner_id:
        owner_id_counter.update(str(owner_id))
        id_counter.update(str(owner_id))
    if comments_user_ids:
        id_counter.update(comments_user_ids)

    # if i % 100 == 0:
    #     with open("vk_dumped.pickle", "wb") as file:
    #         pickle.dump(result, file)

print(owner_id_counter)
print(id_counter)