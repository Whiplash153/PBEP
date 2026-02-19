import json

response_data = {
    "status": "ok",
    "user_id": 42,
    "active": True
}

response_body = json.dumps(response_data)

headers = {
    "Content-Type": "application/json",
    "Content-Length": len(response_body)
}

print("Response headers:", headers)
print("\nResponse body:", response_body)