from datetime import date, datetime

today = date.today()
print("Today's date:", today)

now = datetime.now()
print("Current data and time:", now)

print("Current time only:", now.time())

print("Type of today:", type(today))
print("Type of now:", type(now))