import datetime
import pytz

print("------ fix date with timezone -----")
today = datetime.date.today()
dt = datetime.datetime(2016, 12, 24, 9, 30, 45, 100000, tzinfo=pytz.utc)
print(dt)

print("------ now in utc timezone -----")
dt_now = datetime.datetime.now(pytz.utc)
print(dt_now)

print("------ now in europa timezone -----")
dt_mine = datetime.datetime.now(pytz.timezone('Europe/Berlin'))
print(dt_mine)

print("--------- change timezones -------")
local_date = datetime.datetime.now()
print("timezone unaware", local_date)
print("Europe/Berlin", local_date.astimezone(pytz.timezone('Europe/Berlin')))
print("US/Eastern", local_date.astimezone(pytz.timezone('US/Eastern')))
