import datetime 

# def weekday():
#     q = datetime.datetime.today()   # returns today's date and present time 
#     x = datetime.datetime.today().isocalendar()[1] # isocalander [returns year,week no. of year,day no. of week]
#     y = q.replace(day=1).isocalendar()[1] # returns week no. of year on date = 1 of current month
#     result = (x-y)+1    # sub. week no. of first day of month from week no. of year and adds 1 to give week no. of month
#     return result

# print(weekday())


def user_week_no(date_entry):
    # date_entry = input('Enter a date in YYYY-MM-DD format')
    year, month, day = map(int, date_entry.split('-'))
    date1 = datetime.date(year, month, day)
    x = date1.isocalendar()[1]
    d = date1.replace(day=1).isocalendar()[1]
    result = (x-d)+1
    return result

# print(user_week_no())