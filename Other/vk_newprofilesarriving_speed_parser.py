import urllib.request
from bs4 import BeautifulSoup
import time

a = []
j = 0
temp = 0
opener = urllib.request.build_opener()

while True:
    start_time = time.time()

    url = "https://vk.com/catalog.php"

    soup = BeautifulSoup(opener.open(url).read(), "html.parser")
    time.sleep(0.1)

    url += "?selection=" + BeautifulSoup(opener.open(url).read(), "html.parser").find_all("div", class_="column4")[-1].find_all("a")[-1].text[:3]
    time.sleep(0.1)

    url += "-" + BeautifulSoup(opener.open(url).read(), "html.parser").find_all("div", class_="column4")[-1].find_all("a")[-1].text[4:6]
    time.sleep(0.1)

    url += "-" + BeautifulSoup(opener.open(url).read(), "html.parser").find_all("div", class_="column4")[-1].find_all("a")[-1].text[6:9:2]
    time.sleep(0.1)

    number = int("".join(BeautifulSoup(opener.open(url).read(), "html.parser").find_all("div", class_="column2")[-1].find_all("a")[-1].text[:12].split()))
    time.sleep(0.1)

    elapsed_time = time.time() - start_time

    if j > 1:
        res = (number - temp) / elapsed_time
        print("\t{0:.2f} чел. / сек.".format(res))
        a.append(res)
    if j % 10 == 0 and j != 0:
        print("Среднее значение: {0} человек в секунду.".format((lambda a: sum(a) / len(a))(a)))

    temp = number
    j += 1
    time.sleep(1)
