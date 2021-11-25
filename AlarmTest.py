from time import gmtime, strftime
import time
import datetime
#from alarm import year, month, day, hour, minute, second
import alarm


class AlarmTest():
    def __init__(self, time, date):
        self.time = time
        self.date = date

    def test_date(self):
        isValidDate = True
        try:
            day =self.date[0]
            month=self.date[1]
            year=self.date[2]
            datetime.datetime(day, month, year)
            return "valid date"
            #datetime.datetime(self.date)
            #datetime.datetime.strptime(date, format)  #1st test: tests that the date format is correct
              #2nd test: tests that the selected date is correct

        except ValueError:
            return "invalid date"

    def test_time(self):
       # string_comparison = "test"
        try:
            hour =self.time[0]
            minute=self.time[1]
            second=self.time[2]
            if hour<0 or hour>23 or minute <0 or minute>59 or second<0 or second>59:
                return "invalid time"
            #if (type(self.time) == type(string_comparison)):  #check time type
            if (0 < hour < 24) and (0 < minute < 60) and (0 < second < 60):  #check that the time is valid
                return "valid time"
        except TypeError:
            return "invalid time"

#my_test =AlarmTest([8,22,50],[2021,12,22])
test_list=[]
test1 =AlarmTest([14,37,59],[2021,12,22])
test2 =AlarmTest([8,22,50],[2021,2,30])
test3 =AlarmTest([28,12,41],[2023,4,18])
test4 =AlarmTest([11,75,10],[2023,9,31])
test_list.append(test1)
test_list.append(test2)
test_list.append(test3)
test_list.append(test4)
for i in range(0,len(test_list)):
    print("Test "+str(i+1))
    for test in test_list:
        print(test.test_time())
        print(test.test_date())
        break
    test_list.remove(test)





