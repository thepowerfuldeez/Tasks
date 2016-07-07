import requests, re

#page = requests.post('http://priem.bmstu.ru/ru/me/cabinet/', data={"email" : "И1224", "do-login" : })
print(re.findall(b"/d/d/d", page.content)[:1])