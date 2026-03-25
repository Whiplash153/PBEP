print("=== Full HTTP Parsing ===")

raw_request = """POST /login HTTP/1.1
Host: example.com
Content-Type: application/json
User-Agent: Opera/1.1

{"username": "Misha", "password": "12345"}"""

head, body = raw_request.split("\n\n", 1)

lines = head.split("\n")

start_line = lines[0]

raw_headers = lines[1:]

headers = {}
for line in raw_headers:
    key, value = line.split(": ", 1)
    headers[key] = value

print("Start line:", start_line)
print("Headers:", headers)
print("Body:", body)