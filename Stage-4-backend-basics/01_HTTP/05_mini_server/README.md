# Goal
Understand how a simple HTTP server handles real client requests.
Learn how to catch HTTP methods, paths, headers, and request bodies using Python's built-in `http.server` module.

# What was done
- A minimal HTTP server was implemented using `HTTPServer` and `BaseHTTPRequestHandler`.
- The server handles both GET and POST requests.
- Incoming data is captured:
  - request method  
  - path  
  - headers  
  - body (for POST)
- A logging function was added to store all request details in `requests.log`.

# Notes
This task demonstrates how real HTTP requests look before any frameworks process them.
The server prints request data and also writes it to a log file, simulating basic backend behavior.