raw_request = """GET /any_way HTTP/1.1
Host: misha.ru
User-Agent: Opera/1.1
Accept: text/html
Content-Type: application/json

{"username": "Misha", "password": "12345"}"""

head, body = raw_request.split("\n\n", 1)

lines = head.split("\n")

start_line = lines[0]

headers_raw = lines[1:]

method, path, version = lines[0].split(" ")

headers = {}
for line in headers_raw:
    key, value = line.split(": ", 1)
    headers[key] = value

print("Method:", method)
print("Path:", path)
print("Version:", version)
print("Start line:", start_line)
print("Headers:", headers)
print("Body:", body)