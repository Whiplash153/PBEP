# Goal
The goal of this task was to manually parse a raw HTTP request and extract its main components: the start line, headers, and body. This helps understand how HTTP messages are structured before any framework processes them.

# What was done
A multi-line raw HTTP request string was created and split into two parts: the head (start line and headers) and the body.  
The head was further separated into the start line and individual header lines.  
Each header was parsed into key–value pairs and stored in a dictionary.  
The method, path, HTTP version, headers, and request body were printed for verification.

# Notes
This task demonstrates how HTTP messages look before parsing.  
Headers must follow the `Name: value` format to be processed correctly.  
The empty line separating headers from the body is essential for splitting the message.