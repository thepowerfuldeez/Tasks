"""Доделать парсинг веб-страницы, сделать задержку(сервер не справляется), реализовать сохранение в таблицу"""


import bs4
import urllib.request

BASE_URL = "http://gym5cheb.ru/shkolnaya-zhizn"


def get_html(url):
    response = urllib.request.urlopen(url)
    return response.read()


def get_page_count(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    pagination = soup.find("div", class_="pagination")
    page = pagination.find("p").text

    return int(page.strip()[14:16])


def parse(html):
    soup = bs4.BeautifulSoup(html, "html.parser")
    table_raw = soup.find("table", class_="category table table-striped table-bordered table-hover")
    rows_raw = table_raw.find("tbody").findall("tr")

    projects = []
    for row in rows_raw:
        cols = row.findall("td")

        projects.append({
            "title" : cols[0].find("a").text.strip(),
            "date" : cols[1].text.strip(),
            "views" : cols[2].find("span").text.strip()
        })

    return projects


def main():
    html = get_html(BASE_URL)
    index = 0
    projects = []
    page_count = get_page_count(html)

    for i in range(page_count):
        new_url = BASE_URL + "limit=10&start=" + str(index)
        html = get_html(new_url)
        index += 10

        projects.extend(parse(html))

    print(projects)


if __name__ == "__main__":
    main()
