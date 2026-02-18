from datetime import date, datetime, timedelta

data = input("Enter event date (YYYY-MM-DD): ")

event_date = datetime.strptime(data, "%Y-%m-%d")

print("Event date:", event_date.strftime("%A, %d %B %Y"))

now = datetime.now()
diff = event_date - now

if diff.days < 3:
    print("Reminder: Event is soon!")
else:
    print("You are cool yet")
