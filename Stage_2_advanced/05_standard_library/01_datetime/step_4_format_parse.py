from datetime import datetime

now = datetime.now()

formatted = now.strftime("%d.%m.%Y %H:%M:%S")
print("Formatted datetime:", formatted)

pretty = now.strftime("%A, %d %B %Y")
print("Pretty format:", pretty)

date_str = "2025-11-03 14:30:00"
parsed = datetime.strptime(date_str, "%Y-%m-%d %H:%M:%S")
print("Parsed datetime:", parsed)

print("Type:", type(parsed))