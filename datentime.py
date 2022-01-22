import calendar
import numpy as np
calendar.setfirstweekday(6)

def get_week_of_month(date_entry):
    
    day,month,year = map(int, date_entry.split('/'))
    
    x = np.array(calendar.monthcalendar(year, month))
    week_of_month = np.where(x==day)[0][0] + 1
    
    return(week_of_month)

