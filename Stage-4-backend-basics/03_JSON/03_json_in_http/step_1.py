import json

request_body = """
{
    "username": "Mike",
    "email": "mike@example.com",
    "age": 30
}
"""

print("Raw request body:")
print(request_body)

data = json.loads(request_body)

print("\nParsed data:", data)