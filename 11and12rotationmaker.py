#
# This program is designed to make a  rotating calendar for the American School of Warsaw. 
# The program accounts for vacations, weekends and wednesdays, which have a different meeting time.
# This creates a rotating calendar for student contact days only. 
# This creates output designed to be imported into a google calendar.
#
# A command line scenario might be $11_12rotation.py > 11_12_rotaion.txt
# The txt file would then be imported into google calendar. 
#
# I used this calendar as authoritative reference: 
# https://resources.finalsite.net/images/v1661339384/warsaw/yhzbmoaew1xei49zenyo/ASWCalendar22-23.pdf

# Questions, comments to Bill MacKenty bmackenty@gmail.com
# github repo: https://github.com/bmackenty/rotationMaker.py

# import various libraries:

import datetime
import os
from dateutil.rrule import rrule, DAILY


# initialize the grade 11 and 12 


grade11and12normalPeriod1Start = datetime.time(8,15)
grade11and12normalPeriod1End = datetime.time(9,45)

grade11and12normalPeriod2Start = datetime.time(9,50)
grade11and12normalPeriod2End = datetime.time(11,20)

grade11and12normalPeriod3Start = datetime.time(12,50)
grade11and12normalPeriod3End = datetime.time(14,5)

grade11and12normalPeriodADVStart = datetime.time(11,25)
grade11and12normalPeriodADVEnd = datetime.time(12,5)

grade11and12normalPeriod4Start = datetime.time(14,10)
grade11and12normalPeriod4End = datetime.time(15,40)

# the configuration below is for Wednesdays

grade11and12WednesdayPeriod1Start = datetime.time(9,30)
grade11and12WednesdayPeriod1End = datetime.time(10,50)

grade11and12WednesdayPeriod2Start = datetime.time(11,00)
grade11and12WednesdayPeriod2End = datetime.time(12,20)

grade11and12WednesdayPeriod3Start = datetime.time(12,30)
grade11and12WednesdayPeriod3End = datetime.time(13,50)

grade11and12WednesdayPeriod4Start = datetime.time(14,20)
grade11and12WednesdayPeriod4End = datetime.time(15,40)



# initialization for start of year

startOfAcademicYear = datetime.date(2022,8,18) # Wednesday 
# THIS SHOULD BE THE FIRST MEETING DAY, not the first day of school with a special schedule
endOfAcademicYear = datetime.date(2023,6,15)
academicYearMeetingDays = endOfAcademicYear - startOfAcademicYear

# print("There are", academicYearMeetingDays.days, "total calendar days, including weekends and vacations. ")

# Initialize vacations and staff PD days.  Please triple-check this!!!!

noStudentContactDays = [
	"2022-09-30",
	"2022-10-13",
	"2022-10-14",
	"2022-10-24",
	"2022-10-25",
    "2022-10-26",
    "2022-10-27",
    "2022-10-28",
    "2022-10-31",
    "2022-11-01",
    "2022-11-11",
    "2022-11-24",
    "2022-11-25", 
    "2022-12-19",
    "2022-12-20",
    "2022-12-21",
    "2022-12-22",
    "2022-12-23",
    "2022-12-26",
    "2022-12-27",
    "2022-12-28",
    "2022-12-29",
    "2022-12-30",
    "2023-01-02",
    "2023-01-03",
    "2023-01-04",
    "2023-01-05",
	"2023-01-06",
    "2023-02-20",
    "2023-02-21",
    "2023-02-22",
    "2023-02-23",
    "2023-02-24",
	"2023-03-31",
	"2023-04-06",
	"2023-04-07",
	"2023-04-10",
    "2023-05-01",
	"2023-05-01",
	"2023-05-02",
	"2023-05-03",
	"2023-05-04",
	"2023-05-05",
    "2023-06-08"
    ]
# function to translate interger weekday to human-readable date

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
# Which is kind of silly if you think about it. 
# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
#

# I'm keeping track of some processing data here for sanity 


totalDays = 0
totalDaysNoWeekends = 0 

# this is where we start the year, on a day 1 or A. 

meetingDayNumber = 1

for dt in rrule(DAILY, dtstart=startOfAcademicYear, until=endOfAcademicYear):
		# the condition below skips weekends
		if dt.weekday() < 5:
			if dt.strftime('%Y-%m-%d') not in noStudentContactDays:
				# the condition below limits us to 4 rotating days
				if meetingDayNumber > 4:
					meetingDayNumber = 1
				if meetingDayNumber == 1:
					if dt.weekday() == 2:
						# print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 1,2,3,4")
						print("Blk 1 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Blk 2 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Blk 3 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Blk 4 - Yr 1 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 1,2,3,4")
						print("Blk 1 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Blk 2 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Blk 3 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Blk 4 - Yr 1 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)

				elif meetingDayNumber == 2:
					if dt.weekday() == 2:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 5,6,7,8")
						print("Blk 5 - SCPTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Blk 6 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Blk 7 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Blk 8 - Yr 2 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:	
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 5,6,7,8")
						print("Blk 5 - SCPTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Blk 6 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Blk 7 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Blk 8 - Yr 2 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)

				elif meetingDayNumber == 3:
					if dt.weekday() == 2:	
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 4,2,3,1")
						print("Blk 4 - Yr 1 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Blk 2 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Blk 3 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Blk 1 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 4,2,3,1")
						print("Blk 4 - Yr 1 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Blk 2 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Blk 3 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Blk 1 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)

				elif meetingDayNumber == 4:
					if dt.weekday() == 2:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 8,6,7,5")
						print("Blk 8 - Yr 2 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod1End)
						print("Blk 6 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod2End)
						print("Blk 7 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod3End)
						print("Blk 5 - SCPTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12WednesdayPeriod4End)
					else:
						#print(dt.strftime("%Y-%m-%d"), " is a ", dayOfWeek(dt.weekday()), " which is a day", meetingDay(meetingDayNumber), " which is periods 8,6,7,5")
						print("Blk 8 - Yr 2 CompSci," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod1End)
						print("Blk 6 - DSTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod2End)
						print("Blk 7 - Planning," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod3End)
						print("Blk 5 - SCPTP," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriod4End)
						print("Adv/Comm," ,dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVStart,",",dt.strftime("%m-%d-%Y"),",",grade11and12normalPeriodADVEnd)
				meetingDayNumber += 1
				totalDaysNoWeekends +=1
			totalDays += 1
