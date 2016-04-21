import requests
from bs4 import BeautifulSoup
from collections import Counter

result = []

main_page = requests.get("http://www.problems.ru/view_by_source_new.php?parent=164898").content
soup = BeautifulSoup(main_page, "lxml")

t = soup.find("ul", class_="componentboxlist")
links = t.find_all("a", class_="componentboxlink")
links = [link["href"] for link in links][75:]

for link in links:
    try:
        year_link = "http://www.problems.ru{}".format(link)
        year_page = requests.get(year_link).content
        soup = BeautifulSoup(year_page, "lxml")
        t = soup.find("ul", class_="componentboxlist")
        last_link = [link["href"] for link in t.find_all("a", class_="componentboxlink")][-1]

        problems_page = requests.get("http://www.problems.ru{}".format(last_link)).content
        soup = BeautifulSoup(problems_page, "lxml")
        problems = soup.find_all("table", class_="problemsmallsubjecttable")
        for problem in problems:
            for theme in problem.find_all("a", class_="componentboxlink"):
                result.append(theme.text.strip())
    except:
        pass

print(Counter(result).most_common(20))

