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

# os.system('clear')


#initialization stuff here: 

grade5normalDuty1Start = datetime.time(11,50) 
grade5normalDuty1End = datetime.time(12,10) 

grade5normalDuty2Start = datetime.time(14,45) 
grade5normalDuty2End = datetime.time(15,15) 

grade5normalDuty3Start = datetime.time(11,50) 
grade5normalDuty3End = datetime.time(12,10) 





grade5normalPeriod1Start = datetime.time(8,30) 
grade5normalPeriod1End = datetime.time(8,45) 

grade5normalPeriod2Start = datetime.time(8,50) 
grade5normalPeriod2End = datetime.time(9,30) 

grade5normalPeriod3Start = datetime.time(9,35) 
grade5normalPeriod3End = datetime.time(10,15) 

grade5normalPeriod4Start = datetime.time(10,20) 
grade5normalPeriod4End = datetime.time(11,00) 

grade5normalPeriod5Start = datetime.time(11,5) 
grade5normalPeriod5End = datetime.time(12,30) 

grade5normalPeriod6Start = datetime.time(12,30) 
grade5normalPeriod6End = datetime.time(13,00) 

grade5normalPeriod7Start = datetime.time(12,30) 
grade5normalPeriod7End = datetime.time(13,00) 

grade5normalPeriod8Start = datetime.time(13,00) 
grade5normalPeriod8End = datetime.time(13,50) 

grade5normalPeriod9Start = datetime.time(14,00) 
grade5normalPeriod9End = datetime.time(14,40) 

grade5normalPeriod10Start = datetime.time(14,45) 
grade5normalPeriod10End = datetime.time(15,15) 

grade5normalPeriod11Start = datetime.time(15,20) 
grade5normalPeriod11End = datetime.time(15,30) 


startOfAcademicYear = datetime.date(2019,8,20) # Tuesday
endOfAcademicYear = datetime.date(2020,6,18) # Thursday
academicYearMeetingDays = endOfAcademicYear - startOfAcademicYear

# Initialize vacations and staff PD days.  Please triple-check this!!!!
# These days are are only for the lower-school (sept 26,27 and april 3 are all specific 
# to the lower school 

noStudentContactDays = [
    "2019-09-26",
    "2019-09-27",
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
    "2020-04-03",
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


# for our iterations

totalDays = 0
meetingDay = 0
# 
# These are the headers needed to import the file into google calendar
#
print("Subject,Start Date,Start Time,End Date,End Time")
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
                # print(dayOfWeek(dt.weekday()),",",dt.strftime("%m-%d-%Y"),",",meetingDay)
                if meetingDay == 1:
                    # print("this is the day 1 schedule")
                    print("Student: Music T: Inclusion," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod2End)
                    print("Student: Language T: Ind.," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3End)
                    print("Duty," ,dt.strftime("%m-%d-%Y"),",",grade5normalDuty1Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalDuty1End)

                elif meetingDay == 2:
                    # print("this is the day 1 schedule")
                    print("Student: Language T: Ind.," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3End)
                    print("Student: PE T: RSPP," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4End)

                elif meetingDay == 3:
                    # print("this is the day 1 schedule")
                    print("Student: Art T: PYP," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3End)
                    print("Student: Art T: PYP," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4End)
                    print("Duty," ,dt.strftime("%m-%d-%Y"),",",grade5normalDuty2Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalDuty2End)

                elif meetingDay == 4:
                    # print("this is the day 1 schedule")
                    print("Student: Music T: Ind.," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod2Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod2End)
                    print("Student: Language T:UOI," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3End)

                elif meetingDay == 5:
                    # print("this is the day 1 schedule")
                    print("Student: Language T: Ind.," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3End)
                    print("Student: PE T: Literacy," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4End)
                    print("Duty," ,dt.strftime("%m-%d-%Y"),",",grade5normalDuty3Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalDuty3End)

                elif meetingDay == 6:
                    # print("this is the day 1 schedule")
                    print("Student: Music T:Ind.," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod3End)
                    print("Student: PE T:Math Planning," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod4End)
            else:
                # This must be a wednesday:
                print("Student: PCL T: Ind.," ,dt.strftime("%m-%d-%Y"),",",grade5normalPeriod9Start,",",dt.strftime("%m-%d-%Y"),",",grade5normalPeriod9End)


   
