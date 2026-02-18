import json

task_data = {
    "status": "ready",
    "name": "John",
    "age": 29
}

task_body = json.dumps(task_data)

task_headers = {
    "Content-Type": "application/json",
    "Content-Length": len(task_body)
}

print(task_body)
print(task_headers)