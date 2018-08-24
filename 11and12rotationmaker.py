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

# the configuration below is for Wednesdays

grade9and10WednesdayPeriod1Start = datetime.time(9,30)
grade9and10WednesdayPeriod1End = datetime.time(10,45)

grade9and10WednesdayPeriod2Start = datetime.time(11,00)
grade9and10WednesdayPeriod2End = datetime.time(12,15)

grade9and10WednesdayPeriod3Start = datetime.time(12,55)
grade9and10WednesdayPeriod3End = datetime.time(14,10)

grade9and10WednesdayPeriod4Start = datetime.time(14,15)
grade9and10WednesdayPeriod4End = datetime.time(15,30)



# initialize the grade 11 and 12 


grade11and12normalPeriod1Start = datetime.time(8,20)
grade11and12normalPeriod1End = datetime.time(9,45)

grade11and12normalPeriod2Start = datetime.time(9,50)
grade11and12normalPeriod2End = datetime.time(11,15)

grade11and12normalPeriod3Start = datetime.time(11,30)
grade11and12normalPeriod3End = datetime.time(12,55)

grade11and12normalPeriodADVStart = datetime.time(13,00)
grade11and12normalPeriodADVEnd = datetime.time(13,20)

grade11and12normalPeriod4Start = datetime.time(13,55)
grade11and12normalPeriod4End = datetime.time(15,20)

# the configuration below is for Wednesdays

grade11and12WednesdayPeriod1Start = datetime.time(9,30)
grade11and12WednesdayPeriod1End = datetime.time(10,50)

grade11and12WednesdayPeriod2Start = datetime.time(11,00)
grade11and12WednesdayPeriod2End = datetime.time(12,20)

grade11and12WednesdayPeriod3Start = datetime.time(12,50)
grade11and12WednesdayPeriod3End = datetime.time(14,10)

grade11and12WednesdayPeriod4Start = datetime.time(14,15)
grade11and12WednesdayPeriod4End = datetime.time(15,30)


# Initialize vacations 

vacations = ["2018-09-06","2018-09-07","2018-10-05","2018-10-17","2018-10-29","2018-10-30","2018-10-31","2018-11-01","2018-11-02",
"2018-11-22","2018-11-23",
"2018-12-17","2018-12-18","2018-12-19","2018-12-20","2018-12-21","2018-12-24","2018-12-25","2018-12-26","2018-12-27","2018-12-28","2018-12-31","2019-01-01","2019-01-02","2019-01-03","2019-01-04",
"2019-02-12","2019-02-18","2019-02-19","2019-02-20","2019-02-21","2019-02-22",
"2019-03-15","2019-04-19","2019-04-22","2019-04-29","2019-04-30","2019-05-01","2019-05-02","2019-05-03",
"2019-06-19"]



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

def meetingDay(meetingDayNumber):
	if meetingDayNumber == 1:
		return "A"
	elif meetingDayNumber == 2:
		return "B"
	elif meetingDayNumber == 3:
		return "C"
	elif meetingDayNumber == 4:
		return "D"
	else:
		return "ERROR"
#
# the function below was used from stackoverflow because I wasn't thinking of the date utilities in python.
# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
#

# I'm keeping track of some processing data here for sanity 
#

totalDays = 0
totalDaysNoWeekends = 0 

# this is where we start the year, on a day 1 or A. 

meetingDayNumber = 1

for dt in rrule(DAILY, dtstart=startOfAcademicYear, until=endOfAcademicYear):
		# the condition below skips weekends
		# TODO add 9/10/11/12 split 
		if dt.weekday() < 5:
			if dt.strftime('%Y-%m-%d') not in vacations:
				# the condition below limits us to 4 rotating days
				if meetingDayNumber > 4:
					meetingDayNumber = 1
				if meetingDayNumber == 1:
					if dt.weekday() == 2:
						# print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 1,2,3,4")
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 1,2,3,4")
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)

				elif meetingDayNumber == 2:
					if dt.weekday() == 2:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 5,6,7,8")
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:	
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 5,6,7,8")
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)

				elif meetingDayNumber == 3:
					if dt.weekday() == 2:	
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 4,2,3,1")
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 4,2,3,1")
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)

				elif meetingDayNumber == 4:
					if dt.weekday() == 2:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 8,6,7,5")
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 8,6,7,5")
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)
				meetingDayNumber += 1
				totalDaysNoWeekends +=1
			totalDays += 1
