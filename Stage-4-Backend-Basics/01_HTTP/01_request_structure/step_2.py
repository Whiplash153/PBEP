print("=== Headers ===")

raw_headers = """Host: example.com
User agent: Mozilla/5.0
Accept: text/html
Content-Type: application/json
"""

headers = {}
for line in raw_headers.split("\n"):
    if line.strip():
        key, value = line.split(": ", 1)
        headers[key] = value

print(headers)