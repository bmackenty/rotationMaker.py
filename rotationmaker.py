#
# This program is designed to make a rotating calendar for the American School of Warsaw. 
# 
import datetime
from dateutil.rrule import rrule, DAILY

# initialization stuff for 9th and 10th grade! 

grade9and10normalPeriod1Start = datetime.time(8,30)
grade9and10normalPeriod1End = datetime.time(9,40)

grade9and10normalPeriod2Start = datetime.time(10,00)
grade9and10normalPeriod2End = datetime.time(11,10)

grade9and10normalPeriod3Start = datetime.time(11,20)
grade9and10normalPeriod3End = datetime.time(12,30)

grade9and10normalPeriod4Start = datetime.time(14,20)
grade9and10normalPeriod4End = datetime.time(15,30)

# initialization for start of year

startOfAcademicYear = datetime.date(2018,8,24) # Friday
endOfAcademicYear = datetime.date(2019,6,18) # Wednesday
academicYearMeetingDays = endOfAcademicYear - startOfAcademicYear


# functions to do stuff

def dayOfWeek(integerWeekday):
	if integerWeekday == 0:
		return "Monday"
	elif integerWeekday == 1:
		return "Tuesday"
	elif integerWeekday == 2:
		return "Wednesday"
	elif integerWeekday == 3:
		return "Thursday"
	elif integerWeekday == 4: 
		return "Friday"
	elif integerWeekday == 5: 
			return "Saturday"
	elif integerWeekday == 6: 
			return "Sunday"
	else:
		return "ERROR"			
#
# the function below was used from stackoverflow because I wasn't thinking of the date utilities in python.
# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
#


for dt in rrule(DAILY, dtstart=startOfAcademicYear, until=endOfAcademicYear):
    print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()))







