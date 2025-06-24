import random
import math
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]
year = random.randint(1582, 2023)
month = months[random.randint(0, 11)]

if month == "april" or "june" or "september" or "november":
    day = random.randint(1, 30)
else:
    day = random.randint(1, 31)

if month == "february":
    day = random.randint(1, 28)
if year > 1500:
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
date = [day, month, year]
decade = year % 100
year_adjustment = (math.floor(decade / 4) + decade) % 7

if month == months[0]:
    if decade % 4 == 0:
        weekday = (day + 3) % 7
    else:
        weekday = (day + 4) % 7

if month == months[1]:
    if decade % 4 == 0:
        weekday = day % 7
    else:
        weekday = (day + 1) % 7

if month == months[2] or months[10]:
    weekday = day % 7

if month == months[3] or months[6]:
    weekday = (day + 3) % 7

if month == months[4]:
    weekday = (day + 5) % 7

if month == months[5]:
    weekday = (day + 1) % 7

if month == months[7]:
    weekday = (day + 6) % 7

if month == months[8] or months[11]:
    weekday = (day + 2) % 7

if month == months[9]:
    weekday = (day + 4) % 7

print(date)
print(weekdays[weekday])
