print("=== Body ===")

raw_body = '{"username": "Misha", "password": "12345"}'

print("Raw body:", raw_body)

import json
parsed = json.loads(raw_body)

print("Parsed body:", parsed)
print("Username:", parsed["username"])