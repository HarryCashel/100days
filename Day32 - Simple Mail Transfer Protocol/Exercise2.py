import datetime as dt

now = dt.datetime.now()

# Get the year
year = now.year
print(now)

if year == 2021:
    print(year)

day_of_week = now.weekday()
print(day_of_week)


date_of_birth = dt.datetime(year=1994, month=5, day=1, hour=12)
print(date_of_birth)

