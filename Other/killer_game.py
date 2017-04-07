import random

users = list(range(1, 201))
random.shuffle(users)
users = set(users)
victims_dict = {}

while len(users) > 1:
    user = next(iter(users))
    choice = random.choice(list(users - {user}))
    if choice is None:
        break
    victims_dict[user] = choice
    users.remove(choice)
    users.remove(user)

victims_dict = dict(zip(list(victims_dict.keys()) + list(victims_dict.values()),
                    list(victims_dict.values()) + list(victims_dict.keys())))
print(victims_dict)