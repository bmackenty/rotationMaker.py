#
# This program is designed to make a  rotating calendar for the American School of Warsaw. 
# The program accounts for vacations, weekends and wednesdays, which have a different meeting time.
# This creates a rotating calendar for student contact days only. This creates output designed to be imported into a google calendar.
#
# A command line scenario might be $11_12rotation.py > 11_12_rotaion.txt
# The txt file would then be imported into google calendar. 
#
# I used this calendar as authoritative reference: 
# https://resources.finalsite.net/images/v1539954537/warsaw/kmdb4gksa4mu7rjfwhcj/Calendar2019-2020Final.pdf
#
# Questions, comments to Bill MacKenty bmackenty@gmail.com
# github repo: https://github.com/bmackenty/rotationMaker.py

# import various libraries:

import datetime
import os
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

grade9and10normalPeriodADVStart = datetime.time(13,5)
grade9and10normalPeriodADVEnd = datetime.time(14,15)

grade9and10normalPeriod9Start = datetime.time(13,5)
grade9and10normalPeriod9End = datetime.time(14,15)


# the configuration below is for Wednesdays

grade9and10WednesdayPeriod1Start = datetime.time(9,30)
grade9and10WednesdayPeriod1End = datetime.time(10,45)

grade9and10WednesdayPeriod2Start = datetime.time(11,00)
grade9and10WednesdayPeriod2End = datetime.time(12,15)

grade9and10WednesdayPeriod3Start = datetime.time(12,55)
grade9and10WednesdayPeriod3End = datetime.time(14,10)

grade9and10WednesdayPeriod4Start = datetime.time(14,15)
grade9and10WednesdayPeriod4End = datetime.time(15,30)



# Initialize vacations and staff PD days.  Please triple-check this!!!!

noStudentContactDays = [
	"2019-09-05",
	"2019-09-06",
	"2019-10-04",
	"2019-10-15",
    "2019-10-28",
    "2019-10-29",
    "2019-10-30",
    "2019-10-31",
    "2019-11-01",
    "2019-11-11",
    "2019-11-28",
    "2019-11-29",
    "2019-12-16",
    "2019-12-17",
    "2019-12-18",
    "2019-12-19",
    "2019-12-20",
    "2019-12-23",
    "2019-12-24",
    "2019-12-25",
    "2019-12-26",
    "2019-12-27",
    "2019-12-30",
    "2019-12-31",
    "2020-01-01",
    "2020-01-02",
    "2020-01-03",
    "2020-01-06",
    "2020-02-24",
    "2020-02-25",
    "2020-02-26",
    "2020-02-27",
    "2020-02-28",
	"2020-03-02",
	"2020-04-07",
    "2020-04-10",
    "2020-04-13",
    "2020-04-27",
    "2020-04-28",
    "2020-04-29",
    "2020-04-30",
    "2020-05-01",
    "2020-06-11"
    ]



# initialization for start of year

startOfAcademicYear = datetime.date(2019,8,23) # Friday
endOfAcademicYear = datetime.date(2020,6,18) # Thursday
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
block9onWednesday = False
meetingDayNumber = 1

for dt in rrule(DAILY, dtstart=startOfAcademicYear, until=endOfAcademicYear):
		# the condition below skips weekends
		# TODO add 9/10/11/12 split 
		if dt.weekday() < 5:
			if dt.strftime('%Y-%m-%d') not in noStudentContactDays:
				# the condition below limits us to 4 rotating days
				if meetingDayNumber > 4:
					meetingDayNumber = 1
				if meetingDayNumber == 1:
					if dt.weekday() == 2:
						# print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 1,2,3,4")
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3End)
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 1,2,3,4")
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3End)
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4End)

						if block9onWednesday:
							print("Period 9," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9End)
							block9onWednesday = False
						else:
							print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriodADVEnd)
	
				elif meetingDayNumber == 2:
					if dt.weekday() == 2:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 5,6,7,8")
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3End)
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4End)
						block9onWednesday = True
					else:	
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 5,6,7,8")
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3End)
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4End)
						print("Period 9," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9End)

				elif meetingDayNumber == 3:
					if dt.weekday() == 2:	
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 4,2,3,1")
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3End)
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 4,2,3,1")
						print("Period 4," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1End)
						print("Period 2," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2End)
						print("Period 3," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3End)
						print("Period 1," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4End)
						if block9onWednesday:
							print("Period 9," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9End)
							block9onWednesday = False
						else:
							print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriodADVEnd)
	
				elif meetingDayNumber == 4:
					if dt.weekday() == 2:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 8,6,7,5")
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod3End)
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10WednesdayPeriod4End)
						block9onWednesday = True

					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 8,6,7,5")
						print("Period 8," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod1End)
						print("Period 6," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod2End)
						print("Period 7," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod3End)
						print("Period 5," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod4End)
						print("Period 9," ,dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9Start,",",dt.strftime("%m-%d-%Y"),",",grade9and10normalPeriod9End)
				meetingDayNumber += 1
				totalDaysNoWeekends +=1
			totalDays += 1






# print("I've processed a total of ", totalDays, " days")
# print("I've processed a total of ", totalDaysNoWeekends, " days with no weekends")
