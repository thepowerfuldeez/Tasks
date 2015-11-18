import urllib.request
import urllib.parse
from bs4 import BeautifulSoup
import csv

opener = urllib.request.build_opener()  # to open URL's
opener.addheaders.append(("Cookie",
                          "Session_id="))  # Paste your Session_id from Yandex.Contest after authorisation here

with open("table.csv", "w", newline="") as csvfile:  # It will write results in csv file
    writer = csv.writer(csvfile, delimiter=",", quoting=csv.QUOTE_ALL)
    writer.writerow(["Название", "URL", "Количество участников"])

    for i in range(1, 2000):  # now 2000 is the maximum number of contests available
        try:
            url = "https://contest.yandex.ru/contest/" + str(i) + "/enter/"  # main page url
            new_url = "https://contest.yandex.ru/contest/" + str(i) + "/participants/"  # participants url
            soup = BeautifulSoup(opener.open(url).read().decode("utf-8"), "html.parser")  # open the 1st url
            if ("Зарегистрироваться" or "Вы участвуете в соревновании") in soup.text:
                title = soup.find("title").text.split(" — ")[1]

                part_number = BeautifulSoup(opener.open(new_url).read().decode("utf-8"), "html.parser").find("span",
                                                                            class_="ptp-status__total").text.split()[1]

                writer.writerow([title, url, part_number])
                print("#%d - %s" % (i, title))
        except Exception:
            pass
