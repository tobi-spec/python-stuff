import datetime
import pytz

dt_mine = datetime.datetime.now(pytz.timezone('Europe/Berlin'))

print(dt_mine)
print(dt_mine.isoformat())

print("--------timedate to string----------")
# codes in https://docs.python.org/3/library/datetime.html
string_to_time = dt_mine.strftime("%B %d, %Y")
print(string_to_time)
print(type(string_to_time))

print("----------string to timedate----------")
datetime_to_string = "October 12, 2026"
time_from_string = datetime.datetime.strptime(datetime_to_string, "%B %d, %Y")
print(time_from_string)
print(type(time_from_string))