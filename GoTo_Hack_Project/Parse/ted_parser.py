from bs4 import BeautifulSoup
import requests


class Parser:
    """
    Класс для парсинга страниц. На вход подается id, на выходе из функций можно получить название, просмотры, ключевые
    слова, отметки пользователей и массив всех субтитров.
    """

    def __init__(self, id):
        """
        Инициализирует класс, создается инструмент для открытия сайтов, а также представитель класса BeautifulSoup
        """

        self.id = id
        url = "http://ted.com/talks/{}".format(id)
        default_page = requests.get(url).text
        self.soup = BeautifulSoup(default_page, "lxml")

    def get_title_and_views(self):
        title = self.soup.title.text
        title = title[title.find(":") + 2:-21]  # Обрезаем имя автора и ненужные нам  | TED Talk | TED.com
        views = self.soup.find("span", class_="talk-sharing__value").text.strip()  # Находим число просмотров
        views = int("".join(views.split(",")))  # и преобразуем его в число

        return title, views

    def get_keywords(self):
        topics = [element.text.strip() for element in self.soup.find_all("li", class_="talk-topics__item") if
                  "TED" not in element.text.strip()]
        # Ищет на странице все теги li и выдает текст без пробелов и без вхождений "TED"

        return topics[1:6]

    def get_mood(self):
        s = self.soup.text
        i1 = s.find('"ratings":')  # Первая граница нужных отметок пользователей
        i2 = s.find(',"relatedTalks"')  # Вторая граница
        a = eval(s[i1 + 10:i2])  # Из строки создается массив словарей
        a.sort(key=lambda x: x['count'], reverse=True)  # и сортируется по количеству голосов
        return [x['name'] for x in a[:3]]

    def get_subs(self):
        url = "http://www.ted.com/talks/subtitles/id/{}/lang/ru/format".format(self.id)
        soup = BeautifulSoup(requests.get(url).text, "lxml")
        res = (element.text for element in soup.find_all("a"))  # Возвращает генератор с субтитрами

        return res
