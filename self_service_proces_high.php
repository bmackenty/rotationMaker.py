<?php 

// This program creates a file suitable for importing in google calendar to create a rotating calendar. 
// There are specific rules hard-coded into this program to create rotations for a specific school scenario
// TODO: make a full academic calendar for whole year to check. 
// This code is stored on github

$block_1 = $_POST['block_1'];
$block_2 = $_POST['block_2'];
$block_3 = $_POST['block_3'];
$block_4 = $_POST['block_4'];
$block_5 = $_POST['block_5'];
$block_6 = $_POST['block_6'];
$block_7 = $_POST['block_7'];
$block_8 = $_POST['block_8'];
$block_9 = $_POST['block_9'];

# this section was for debugging passed values:

    // echo "I have: <br>";
    // echo "$block_1 <br />";
    // echo "$block_2 <br />";
    // echo "$block_3 <br />";
    // echo "$block_4 <br />";
    // echo "$block_5 <br />";
    // echo "$block_6 <br />";
    // echo "$block_7 <br />";
    // echo "$block_8 <br />";
    // echo "$block_9 <br />";


$noStudentContactDays = array(
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
);

if (in_array($noStudentContactDays,"2020-06-11")) {
    echo "there is a date in no student contact days";
}

# Because I'm not doing any calculations or weird stuff with these times, I'm keeping them as strings. 
# I had them as datetime objects, but it didn't make sense for an end-product that is imported as a CSV
# into google. 

$grade9and10normalPeriod1Start = "8:30";
$grade9and10normalPeriod1End = "9:40";

$grade9and10normalPeriod2Start = "10:00";
$grade9and10normalPeriod2End = "11:10";

$grade9and10normalPeriod3Start = "11:20";
$grade9and10normalPeriod3End = "12:30";

$grade9and10normalPeriod4Start = "14:20";
$grade9and10normalPeriod4End = "15:30";

$grade9and10normalPeriodADVStart = "13:05";
$grade9and10normalPeriodADVEnd = "14:15";

$grade9and10normalPeriod9Start = "13:05";
$grade9and10normalPeriod9End = "14:15";


# the configuration below is for Wednesdays

$grade9and10WednesdayPeriod1Start = "9:30";
$grade9and10WednesdayPeriod1End = "10:45";

$grade9and10WednesdayPeriod2Start = "11:00";
$grade9and10WednesdayPeriod2End = "12:15";

$grade9and10WednesdayPeriod3Start = "12:55";
$grade9and10WednesdayPeriod3End = "14:10";

$grade9and10WednesdayPeriod4Start = "14:15";
$grade9and10WednesdayPeriod4End = "15:30";


# initialization for start of year 

$startOfAcademicYear = new datetime('2019-08-23'); # Friday
$endOfAcademicYear = new datetime('2020-06-18'); # Thursday

$interval = DateInterval::createFromDateString("1 day");
$period = new DatePeriod($startOfAcademicYear, $interval, $endOfAcademicYear);

$current_meeting_day = 0;

# day 1 = A
# day 2 = B
# day 3 = C
# day 4 = D
# the format we follow is from google: description, start date, start time, end date, end time. 
echo "Description,Start Date, Start Time, End Date, End Time<br />";



foreach ($period as $dt) {
    $current_day = $dt->format("Y-m-d");
    if ($dt->format("l") == "Saturday" || $dt->format("l") == "Sunday") {
        # we dont want weekends, so this is blank
    } elseif (in_array($current_day,$noStudentContactDays)) {
        # we don't want any days in the no student contact days, so this blank
    } else {
        # with no weekends or student contact days, this should represent school meeting days
        $counter +=1;
        echo "Day $current_meeting_day " .  $dt->format("l") . " -> ";
        echo "<br />";
        $current_meeting_day += 1;
        # The condition below keeps our rotation at 4 days
        if ($current_meeting_day == 5) {
            $current_meeting_day = 1;
        }
        if ($current_meeting_day == 1) {
            # this is a day A
            # day A has block 1,2,3,4 in that order 
            if ($dt->format("l") != "Wednesday") {
                # Below is the Monday, Tuesday, Thursday and Friday schedule for day A: 
                echo "$block_1, $current_day, $grade9and10normalPeriod1Start, $current_day, $grade9and10normalPeriod1End";
                echo "<br />";
                echo "$block_2, $current_day, $grade9and10normalPeriod2Start, $current_day, $grade9and10normalPeriod2End";
                echo "<br />";
                echo "$block_3, $current_day, $grade9and10normalPeriod3Start, $current_day, $grade9and10normalPeriod3End";
                echo "<br />";
                echo "$block_4, $current_day, $grade9and10normalPeriod4Start, $current_day, $grade9and10normalPeriod4End";
                echo "<br />";
                if ($block_9_on_wednesday) {
                    # if a block 9 happens on a Wednesday, the following day there is block 9 during advisory. 
                    echo "$block_9, $current_day, $grade9and10normalPeriodADVStart, $current_day, $grade9and10normalPeriodADVEnd";
                    echo "<br />";
                    $block_9_on_wednesday = false;
                }
            } else {
                # Below is the Wednesday schedule for day A: 
                echo "$block_1, $current_day, $grade9and10WednesdayPeriod1Start, $current_day, $grade9and10WednesdayPeriod1End";
                echo "<br />";
                echo "$block_2, $current_day, $grade9and10WednesdayPeriod2Start, $current_day, $grade9and10WednesdayPeriod2End";
                echo "<br />";
                echo "$block_3, $current_day, $grade9and10WednesdayPeriod3Start, $current_day, $grade9and10WednesdayPeriod3End";
                echo "<br />";
                echo "$block_4, $current_day, $grade9and10WednesdayPeriod4Start, $current_day, $grade9and10WednesdayPeriod4End";
                echo "<br />";
            }
        } else if ($current_meeting_day == 2) {
            # this is a day B
            # day B has block 5,6,7,9,8 in that order
            # But if block 9 falls on a Wednesday, there is no block 9 and it instead meets on the next day. 
            # Below is the Monday, Tuesday, Thursday and Friday schedule for day B:
                if ($dt->format("l") != "Wednesday") { 
                    echo "$block_5, $current_day, $grade9and10normalPeriod1Start, $current_day, $grade9and10normalPeriod1End";
                    echo "<br />";
                    echo "$block_6, $current_day, $grade9and10normalPeriod2Start, $current_day, $grade9and10normalPeriod2End";
                    echo "<br />";
                    echo "$block_7, $current_day, $grade9and10normalPeriod3Start, $current_day, $grade9and10normalPeriod3End";
                    echo "<br />";
                    echo "$block_9, $current_day, $grade9and10normalPeriod9Start, $current_day, $grade9and10normalPeriod9End";
                    echo "<br />";
                    echo "$block_8, $current_day, $grade9and10normalPeriod4Start, $current_day, $grade9and10normalPeriod4End";
                    echo "<br />";
            } else {
                    # Below is the Wednesday schedule for day B: 
                    echo "$block_5, $current_day, $grade9and10WednesdayPeriod1Start, $current_day, $grade9and10WednesdayPeriod1End";
                    echo "<br />";
                    echo "$block_6, $current_day, $grade9and10WednesdayPeriod2Start, $current_day, $grade9and10WednesdayPeriod2End";
                    echo "<br />";
                    echo "$block_7, $current_day, $grade9and10WednesdayPeriod3Start, $current_day, $grade9and10WednesdayPeriod3End";
                    echo "<br />";
                    echo "$block_8, $current_day, $grade9and10WednesdayPeriod4Start, $current_day, $grade9and10WednesdayPeriod4End";
                    echo "<br />";
                    $block_9_on_wednesday = true;
            }
        }  else if ($current_meeting_day == 3) {
        # this is a day C
        # day C has block 4,2,3,1 in that order
        # Below is the Monday, Tuesday, Thursday and Friday schedule for day C:
            if ($dt->format("l") != "Wednesday") { 
                echo "$block_4, $current_day, $grade9and10normalPeriod1Start, $current_day, $grade9and10normalPeriod1End";
                echo "<br />";
                echo "$block_2, $current_day, $grade9and10normalPeriod2Start, $current_day, $grade9and10normalPeriod2End";
                echo "<br />";
                echo "$block_3, $current_day, $grade9and10normalPeriod3Start, $current_day, $grade9and10normalPeriod3End";
                echo "<br />";
                echo "$block_1, $current_day, $grade9and10normalPeriod4Start, $current_day, $grade9and10normalPeriod4End";
                echo "<br />";
                if ($block_9_on_wednesday) {
                    # if a block 9 happens on a Wednesday, the following day there is block 9 during advisory. 
                    echo "$block_9, $current_day, $grade9and10normalPeriodADVStart, $current_day, $grade9and10normalPeriodADVEnd";
                    echo "<br />";
                    $block_9_on_wednesday = false;
                }
        } else {
                # Below is the Wednesday schedule for day C: 
                echo "$block_4, $current_day, $grade9and10WednesdayPeriod1Start, $current_day, $grade9and10WednesdayPeriod1End";
                echo "<br />";
                echo "$block_2, $current_day, $grade9and10WednesdayPeriod2Start, $current_day, $grade9and10WednesdayPeriod2End";
                echo "<br />";
                echo "$block_3, $current_day, $grade9and10WednesdayPeriod3Start, $current_day, $grade9and10WednesdayPeriod3End";
                echo "<br />";
                echo "$block_1, $current_day, $grade9and10WednesdayPeriod4Start, $current_day, $grade9and10WednesdayPeriod4End";
                echo "<br />";
        }
    } else if ($current_meeting_day == 4) {
    # this is a day D
    # day D has block 8,6,7,9,5 in that order
    # Below is the Monday, Tuesday, Thursday and Friday schedule for day D:
        if ($dt->format("l") != "Wednesday") { 
            echo "$block_8, $current_day, $grade9and10normalPeriod1Start, $current_day, $grade9and10normalPeriod1End";
            echo "<br />";
            echo "$block_6, $current_day, $grade9and10normalPeriod2Start, $current_day, $grade9and10normalPeriod2End";
            echo "<br />";
            echo "$block_7, $current_day, $grade9and10normalPeriod3Start, $current_day, $grade9and10normalPeriod3End";
            echo "<br />";
            echo "$block_9, $current_day, $grade9and10normalPeriod9Start, $current_day, $grade9and10normalPeriod9End";
            echo "<br />";
            echo "$block_5, $current_day, $grade9and10normalPeriod4Start, $current_day, $grade9and10normalPeriod4End";
            echo "<br />";
        } else {
                # Below is the Wednesday schedule for day D: 
                echo "$block_8, $current_day, $grade9and10WednesdayPeriod1Start, $current_day, $grade9and10WednesdayPeriod1End";
                echo "<br />";
                echo "$block_6, $current_day, $grade9and10WednesdayPeriod2Start, $current_day, $grade9and10WednesdayPeriod2End";
                echo "<br />";
                echo "$block_7, $current_day, $grade9and10WednesdayPeriod3Start, $current_day, $grade9and10WednesdayPeriod3End";
                echo "<br />";
                echo "$block_5, $current_day, $grade9and10WednesdayPeriod4Start, $current_day, $grade9and10WednesdayPeriod4End";
                echo "<br />";
                $block_9_on_wednesday = True;
        }
    }
        echo "<br>";
    }

}
echo "Total meeting days: $counter";
