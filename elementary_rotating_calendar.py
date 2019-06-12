#
# This program is designed to make a 6 day rotating calendar for the American School of Warsaw. 
# The program accounts for vacations, weekends, and wacky wednesdays, which does not count as a 6 day rotating day.
# This creates a rotating calendar for student ocntact days only! 
# I used this calendar as authoritative reference: https://resources.finalsite.net/images/v1539954537/warsaw/kmdb4gksa4mu7rjfwhcj/Calendar2019-2020Final.pdf
#
# Questions, comments to Bill MacKenty bmackenty@gmail.com
# github repo: https://github.com/bmackenty/rotationMaker.py

# import various libraries:

import os
import datetime
from dateutil.rrule import rrule, DAILY

# this just clears the screen for my own sanity:

os.system('clear')

# initialization for start of year

startOfAcademicYear = datetime.date(2019,8,20) # Tuesday
endOfAcademicYear = datetime.date(2020,6,18) # Thursday
academicYearMeetingDays = endOfAcademicYear - startOfAcademicYear

print("There are", academicYearMeetingDays.days, "total calendar days, including weekends and vacations. ")

# Initialize vacations and staff PD days.  Please triple-check this!!!! 

noStudentContactDays = [
    "2019-10-04",
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
    "2020-04-10",
    "2020-04-13",
    "2020-04-27",
    "2020-04-28",
    "2020-04-29",
    "2020-04-30",
    "2020-05-01",
    "2020-06-11"
    ]


# meeting days work like this: 

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


# I'm keeping track of some processing data here for sanity: 

startingMeetingDay = 1
totalDays = 0
totalDaysNoWeekends = 0 
meetingDay = 0


#
# the loop below was used from stackoverflow because I wasn't thinking of the date utilities in python.
# https://stackoverflow.com/questions/1060279/iterating-through-a-range-of-dates-in-python
#

for dt in rrule(DAILY, dtstart=startOfAcademicYear, until=endOfAcademicYear):
    # the condition below skips weekends:
    if dt.weekday() < 5:
        # the condition below skips any days defined in no contact days: 
        if dt.strftime('%Y-%m-%d') not in noStudentContactDays:
            # count total contact days: 
            totalDays += 1
            # the condition below skips Wednesdays:
            if dt.weekday() != 2:
                # now we reset the rotation if it is higher than 6:
                if meetingDay == 6:
                    meetingDay = 0
                meetingDay += 1
                print(dayOfWeek(dt.weekday()), ",", dt.strftime("%m-%d-%Y") , "Rotating day: ", meetingDay)


print("Total student contact days (counting Wednesdays): ", totalDays)
