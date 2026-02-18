from storage_json import Storage
from models import Task

storage = Storage("tasks.json")

task1 = Task(id=1, title="Buy milk")
task2 = Task(id=2, title="Write code")

storage.add(task1)
storage.add(task2)

print("After adding:")
for task in storage.all():
    print(task.id, task.title)
