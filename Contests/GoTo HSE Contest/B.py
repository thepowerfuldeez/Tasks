import datetime

year = int(input())
for i in range(30, 21, -1):
    if datetime.datetime(year, 11, i).weekday() == 6:
        print(i)
        break
