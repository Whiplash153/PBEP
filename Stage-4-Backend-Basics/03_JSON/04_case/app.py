import json

# --- INCOMING HTTP request ---
request_body = """
{
    "name": "John",
    "age": 29
}
"""

print("Incoming request body:", request_body)

# --- server parses JSON ---
data = json.loads(request_body)

print("Parsed request data:", data)

if data["age"] >= 18:
    result = {
        "status": "ok",
        "message": "Access granted"
    }
else:
    result = {
        "status": "rejected",
        "message": "Access denied"
    }

print("\nBusiness logic result:", result)

# --- serialize ---
response_body = json.dumps(result)

# --- server response ---
headers= {
    "Content-Type": "application/json",
    "Content-Length": len(response_body)
}

print("\nResponse body:", response_body)
print("\nResponse headers:", headers)
