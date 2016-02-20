import csv
import sys
from ted_parser import Parser
from text_analyzer import Analyzer
from pymystem3 import Mystem

sys.setrecursionlimit(5000)


def work(n, i=1):  # На практике ~2 сек. На всю работу ~ 1.5 ч. x3
    if i > n:
        return
    try:
        print(i)
        p = Parser(i)  # Парсер инициализирован за 0.656

        title, views = p.get_title_and_views()  # Заголовок и кол-во просмотров спаршены за 0.004
        mood = p.get_mood()  # Настроения пользователей спаршены за 0.001
        keywords = p.get_keywords()  # Ключевые слова спаршены за 0.008

        subs = p.get_subs()  # Субтитры получены за 0.329
        text_array = m.lemmatize(" ".join(subs))  # Субтитры простеммлены за 0.104
        top20 = Analyzer(text_array).start()  # Обработка субтитров за 0.461

        writer.writerow([i, title, views, " ".join(mood), " ".join(top20)])
        writer_keywords.writerow([i, " ".join(keywords)])
        work(n, i + 1)
    except:
        work(n, i + 1)


with open("main_table.csv", "w", newline="") as csvfile, open("keywords_table.csv", "w",
                                                              newline="") as csvfile_keywords:
    writer = csv.writer(csvfile, delimiter=";", quoting=csv.QUOTE_ALL)
    writer_keywords = csv.writer(csvfile_keywords, delimiter=";", quoting=csv.QUOTE_ALL)
    writer.writerow(["ID", "Название", "Кол-во просмотров", "Настроение", "ТОП10 Слов"])
    writer_keywords.writerow(["ID", "Ключевые слова"])

    m = Mystem()
    work(2346)  # 2346
