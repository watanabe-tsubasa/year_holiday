import datetime

test_day = datetime.date(2023, 5, 20)

while True:
    print(test_day)
    print(test_day.day)
    if test_day.weekday() in [5,6]:
        print('holiday')
    test_day += datetime.timedelta(days=1)
    if test_day.day == 20:
        break