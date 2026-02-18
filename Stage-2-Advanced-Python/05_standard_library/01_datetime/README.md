# Datetime Mini-Practice — Event Reminder

## Goal
Practice using Python's `datetime` module to calculate date differences and format output.

## Description
The program:
- asks the user to enter an event date in the format `YYYY-MM-DD`,
- parses the input string into a `datetime` object using `strptime`,
- compares it to the current date and time (`datetime.now()`),
- and prints one of two messages:
  - 🔴 if less than 3 days remain before the event;
  - 🟢 if the event is more than 3 days away.

Also formats the event date into a human-readable string using `strftime("%A, %d %B %Y")`.