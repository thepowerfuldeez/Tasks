import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import lxml
import csv

opener = urllib.request.build_opener()  # to open URL's
opener.addheaders.append(("Cookie",
                          "Session_id=3:1453190014.5.0.1452858600974:olfVsA:4f.0|116308269.0.2|140091.142040.4QkOQqVmExBr7_lIKJw_zT4vdiI"))  # Paste your Session_id from Yandex.Contest after authorisation here

with open("table.csv", "w", newline="") as csvfile:  # It will write results in csv file
    writer = csv.writer(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)
    writer.writerow(["Название", "URL", "Количество участников"])

    for i in range(1, 3000):  # now 3000 is the maximum number of contests available
        try:
            url = "https://contest.yandex.ru/contest/" + str(i) + "/enter/"  # main page url
            new_url = "https://contest.yandex.ru/contest/" + str(i) + "/participants/"  # participants url
            soup = BeautifulSoup(opener.open(url).read().decode("utf-8"), "html.parser")  # open the 1st url
            if ("Зарегистрироваться" or "Задачи") in soup.text:
                title = soup.find("title").text.split(" — ")[1]

                part_number = BeautifulSoup(opener.open(new_url).read().decode("utf-8"), "html.parser").find("span",
                                                                            class_="ptp-status__total").text.split()[1]

                writer.writerow([title, url, part_number])
                print("\tПарсинг. {:.2%} процентов завершено".format(i / 2000))
        except Exception:
            pass
