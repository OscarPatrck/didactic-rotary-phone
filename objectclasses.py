import math
import random
import time

total_time = 0
current_time = time.time()
start_time = time.time()
turn = 0
score = 0


def display_time(input_period, output_preamble):
    seconds = input_period % 60
    minutes = (input_period - seconds) / 60
    if minutes == 0:
        print(f"{output_preamble}: {input_period:.0f} seconds.")
    if minutes == 1:
        print(f"{output_preamble}: {minutes:.0f} minute {seconds:.0f} seconds.")
    if minutes > 1:
        print(f"{output_preamble}: {minutes:.0f} minutes {seconds:.0f} seconds.")


while turn < 10:
    month = random.randint(1, 12)
    year = random.randint(1582, 2099)
    feblength = 28
    if year % 4 == 0:
        feblength = 29
    if year % 100 == 0:
        feblength = 28
    if year % 400 == 0:
        feblength = 29

    if month == 4 or 6 or 9 or 11:
        date = random.randint(1, 30)
    else:
        date = random.randint(1, 31)

    if month == 2:
        date = random.randint(1, feblength)


    class Month:
        def __init__(self, length, name):
            self.length = length
            self.name = name


    months = [Month(31, "January"),
              Month(feblength, "February"),
              Month(31, "March"),
              Month(30, "April"),
              Month(31, "May"),
              Month(30, "June"),
              Month(31, "July"),
              Month(31, "August"),
              Month(30, "September"),
              Month(31, "October"),
              Month(30, "November"),
              Month(31, "December")]
    days_up_to_this_month = 0
    for n in range(0, month - 1):
        days_up_to_this_month = days_up_to_this_month + months[n].length

    days_this_year = days_up_to_this_month + date
    starting_day = 3
    if year > 1600:
        starting_day = 2
    if year > 1700:
        starting_day = 0
    if year > 1800:
        starting_day = 5
    if year > 1900:
        starting_day = 3
    if year > 2000:
        starting_day = 2

    total_days = starting_day + days_this_year + (year % 100) + math.floor((year % 100) / 4) - 3
    if feblength == 29 and (month == 2 or 1):
        total_days = total_days - 1
    days_of_the_week = ["su", "mo", "tu", "we", "th", "fr", "sa"]
    print(date, months[month - 1].name, year)
    if input() == days_of_the_week[total_days % 7]:
        score = score + 1
    print(days_of_the_week[total_days % 7])
    end_time = time.time()
    elapsed_time = end_time - current_time
    display_time(elapsed_time, "time")
    total_time = elapsed_time + total_time
    current_time = time.time()
    turn = turn + 1

print(score, "/", turn, sep="")
average_time = total_time/10
display_time(average_time, "average time")
# january is buggy, I think only on leap years... fixed!
# need to add minutes and seconds then add feature for average time done
