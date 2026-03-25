import sys
import requests

print("Python version:", sys.version)

response = requests.get("https://httpbin.org/get")
print("Status code:", response.status_code)
print("Responce JSON:", response.json())