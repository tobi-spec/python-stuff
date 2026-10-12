import datetime

# naive times = don´t have timezones/ daylight saving times
# aware times = have timezones/ daylight saving times

print("--------- date ---------")
date = datetime.date(2016, 4, 7)
print(date)
print(type(date))

print ("----- date - today-------")
today = datetime.date.today()
print(today)
print(today.year)
print(today.weekday()) # monday starts at 0
print(today.isoweekday()) # monday starts at 1

print("-------- time delta --------")
time_delta = datetime.timedelta(days=7)
print(time_delta)

date2 = today + time_delta
print(date2)

chrismas = datetime.date(2026, 12, 24)
till_christmas = chrismas - today
print(till_christmas)

print("--------- time --------")
time = datetime.time(9, 30, 45, 100000)
print(time)

print ("------ date and time --------")
datetime = datetime.datetime(2016, 12, 24, 9, 30, 45, 100000)
print(datetime)
print(datetime.time())
print(datetime.date())
print(datetime.weekday())

print(datetime.today()) # current local datetime without timezone
print(datetime.now()) # current local datetime with optional timezone

