import json
from models import HomeTask
from pathlib import Path

class Storage:
    def __init__(self, filepath):
        self._items = []
        self._filepath = Path(filepath)
        self.load()

    def add_task(self, task):
        if not self._items:
            last_id = 0
        else:
            last_id = max(task.id for task in self._items)

        new_id = last_id + 1
        task.id = new_id
        self._items.append(task)
        self.save()

    def load(self):
        if not self._filepath.exists():
            return
        else:
            with open(self._filepath, "r", encoding="utf-8") as f:
                raw_items = json.load(f)

        self._items = [HomeTask.from_dict(data) for data in raw_items]

    def save(self):
        with open(self._filepath, "w", encoding="utf-8") as f:
            data = [item.to_dict() for item in self._items]
            json.dump(data, f, ensure_ascii=False, indent=2)

    def get_all_tasks(self):
        return list(self._items)

    def get_task_by_id(self, task_id):
        for task in self._items:
            if task.id == task_id:
                return task
        raise ValueError("No such task id")





