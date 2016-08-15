#!/usr/bin/python3.4


def main():
    import xlrd
    import re
    from firebase import firebase

    rb = xlrd.open_workbook("/home/thepowerfuldeez/Downloads/table.xls")
    sheet = rb.sheet_by_index(0)

    floating_number = re.compile("[0-9]+\.0")
    group_name = re.compile("[а-яА-Я]+[1-8]")

    def get_float_lesson_number(text):
        return re.findall(floating_number, text)[0]

    def get_easy_rows():
        easy_rows = []
        for rownum in range(sheet.nrows):
            x = " ".join([str(i) for i in sheet.row_values(rownum)])
            try:
                text_float_number = get_float_lesson_number(x)
            except IndexError:
                continue
            number = int(float(text_float_number))
            if 0 < number < 11:
                easy_rows.append([i.strip() for i in x.split(text_float_number) if i][-2:])
        return easy_rows

    def turn_normal(a):
        """Превращает Общество О2- 103, 'Математика М1 - 309, М2 - 101, М3 - 107 в О2, М1 М2 М3"""
        return " ".join(re.findall(group_name, a[0])).upper(), " ".join(re.findall(group_name, a[1])).upper()

    days_map = {}
    a = get_easy_rows()
    for i in range(len(a)):
        b = a[i]
        last_2_letters = b[1][-2:].upper()
        if last_2_letters in "ПНВТСРЧТПТСБ":
            normal = []
            t = a[i:i + 10]
            for x in t:
                normal.append(turn_normal(x))
            days_map[last_2_letters] = normal

    def get_class_lessons(day, class_n):
        if class_n == 10:
            i = 0
        elif class_n == 11:
            i = 1

        a = days_map[day.upper()]
        return ";".join(x[i] for x in a)

    firebase_ref = firebase.FirebaseApplication('https://gym5meetings.firebaseio.com', None)
    firebase_ref.delete("/schedule/11", None)
    firebase_ref.delete("/schedule/10", None)
    for day in ("пн", "вт", "ср", "чт", "пт", "сб"):
        for class_number in (10, 11):
            result = get_class_lessons(day, class_number)
            firebase_ref.put('/schedule/{}/{}'.format(str(class_number), day), "subjects", result)
            # print("Расписание {}-го класса на {}: {}".format(class_number, day, result))

main()