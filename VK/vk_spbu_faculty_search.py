import pandas as pd
from vk_core import Vk

vk = Vk()

# SPBU ID = 1
# MathMech faculty ID = 7
# PMPU faculty ID = 11
# Chem. faculty ID = 17
# Phys. faculty ID = 14
# Economics faculty ID = 18


def get_users(faculty, year):
    r = vk.method("users.search", {
        "sort": 0,
        "count": 1000,
        "fields": "sex,last_seen,can_write_private_message",
        "university": 1,
        "university_year": year,
        "university_faculty": faculty
    })['items']
    return pd.DataFrame({"id": q['id'], "sex": q['sex'], "year": year, "faculty": faculty, "messages": q['can_write_private_message'], "last_seen": q['last_seen']["time"]} for q in r)

df = get_users(7, 2020)
for faculty_ in [11, 17, 14, 18]:
    df = df.append(get_users(faculty_, 2020))

for year_ in range(2017, 2020):
    for faculty_ in [7, 11, 17, 14, 18]:
        df = df.append(get_users(faculty_, year_))

df.to_csv("students.csv")

