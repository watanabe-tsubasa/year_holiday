import csv
import datetime

def generate_holiday_list(path:str):
    holiday_list = []
    with open(path) as f:
        reader = csv.reader(f)
        for row in reader:
            add_date = datetime.datetime.strptime(row[0], '%Y/%m/%d').date()
            holiday_list.append(add_date)
    
    return holiday_list
        
def count_days(holiday_list:list, year:int, month:int, day:int=20):
    try:
        current_day = datetime.datetime(year, month - 1, day).date()
    except:
        current_day = datetime.datetime(year-1, 12, day).date()
    day_count = 0
    holiday_count = 0
    
    def is_holiday(holiday_list:list, current_day:datetime.date):
        if current_day in holiday_list:
            return True
        elif current_day.weekday() in [5,6]:
            return True
        else:
            return False
    
    while True:
        day_count += 1
        if is_holiday(holiday_list, current_day):
            holiday_count += 1
        current_day += datetime.timedelta(days=1)
        if current_day.day == day:
            break
    
    return (day_count, holiday_count, 8 * (day_count - holiday_count) )

year = 2023
month = 7
next_month = 1
holiday_list = generate_holiday_list(f'./data/{year}_holiday.csv')

while month < 13:
    print(f'{month}: {count_days(holiday_list,year,month)}')
    month += 1
while next_month < 7:
    print(f'{next_month}: {count_days(holiday_list, year + 1, next_month)}')
    next_month += 1