from datetime import date, time, datetime

birthday = date(1998, 7, 12)
print("\nBirthday:", birthday)

alarm_time = time(7, 30, 0)
print("Alarm time:", alarm_time)

meeting = datetime(2025, 11, 3, 14, 0, 0)
print("Meeting:", meeting)

print("\nMeeting year:", meeting.year)
print("Meeting month:", meeting.month)
print("Meeting day:", meeting.day)
print("Meeting hour:", meeting.hour)
print("Meeting minute:", meeting.minute)
