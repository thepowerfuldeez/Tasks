from textblob import TextBlob
from PyDictionary import PyDictionary
import csv

"""Всего работа заняла 12 часов"""
with open('main_table.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    words2d = [{i[0] : i[-1]} for i in reader]

pd = PyDictionary()
enhanced_word_sets = []  # Дополненные списки слов(включая синонимы) - обычно в 5 раз длиннее
MATRIX = [[0]*2346]*2346

for words in words2d[1:]:
    res = set()
    id = [int(i) for i in words.keys()][0]
    if words:
        for value in words.values():  # Обходим каждое слово, превращаем его в синонимы, добавляем в сет
            en_words = [word for word in TextBlob(value).translate("ru").split() if word not in
"a about an are as at be by com for from how in is it of on or that the this to was what when where who will with the"]
            rus_synonyms = ""
            for word in en_words:
                synonyms = pd.synonym(word.split()[-1])
                if synonyms:
                    rus_synonyms += " ".join(synonyms) + " "
        for word in TextBlob(rus_synonyms).translate("en", "ru").split():
            res.add(word)

    print("Завершено создание расширенного списка слов для", id, "из 2346")
    enhanced_word_sets.append((id, res))

i = 1
for set_ in enhanced_word_sets:
    for _set in enhanced_word_sets:
        _id_ = set_[0], _set[0]
        if not _id_[0] == _id_[1]:
            index = len(set_[1] & _set[1]) / len(set_[1] | _set[1])  # Индекс схожести
            if 0.25 <= index < 1:
                MATRIX[_id_[0]][_id_[1]] = 1
    print(i, end=" ")
    i += 1

print("Работа выполнена, начинается запись в файл")
with open("RESULT.csv", "w") as RESULTCSV:
    writer = csv.writer(RESULTCSV, delimiter=";", quoting=csv.QUOTE_ALL)
    for row in MATRIX:
        writer.writerow(row)