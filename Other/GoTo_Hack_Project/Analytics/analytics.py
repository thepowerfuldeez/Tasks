import csv
from collections import Counter

with open('main_table.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    words = []
    marks = []
    for line in reader:
        for word in line[-1].split():
            words.append(word)
        marks.append(line[-2])

with open("RESULT.csv", "w") as res_csv:
    print("Слово", "Количество", file=res_csv, sep=";")
    for line in Counter(words[1:]).most_common(50):
        print(line[0], line[1], file=res_csv, sep=";")