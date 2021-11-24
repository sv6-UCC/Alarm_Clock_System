from time import gmtime, strftime
import time
import datetime
from alarm import year, month, day, hour, minute, second

format = "d-%m-%Y"

class AlarmTest():
    def __init__(self, time, date):
        self.time = time
        self.date = date

    def test_date(date):
        isValidDate = True
        try:
            datetime.datetime.strptime(date, format)  #1st test: tests that the date format is correct 
            datetime.datetime(int(year.get()), int(month.get()), int(day.get()))  #2nd test: tests that the selected date is correct  
        except ValueError:
            isValidDate = False

    def test_time(time): 
        string_comparison = "test"
        try: 
            if (type(time) == type(string_comparison)):  #check time type
                if (0 < hour.get() < 24) and (0 < minute.get() < 60) and (0 < second.get() < 60):  #check that the time is valid 
                    return "valid time"
        except TypeError:
            return "invalid time"




