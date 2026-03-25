import requests

response = requests.get("https://httpbin.org/get")
print("Status code:", response.status_code)
print("Response JSON:", response.json())