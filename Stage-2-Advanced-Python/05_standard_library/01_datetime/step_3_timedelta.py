from datetime import datetime, timedelta

now = datetime.now()
print("Now:", now)

delta = timedelta(days=5)
print("Timedelta:", delta)

future = now + delta
past = now - delta

print("5 days earlier:", past)
print("5 days later:", future)

new_year = datetime(now.year + 1, 1, 1)
remaining = new_year - now
print("Days until new year:", remaining.days)