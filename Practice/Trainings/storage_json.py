import json
from pathlib import Path
from models import Task

class Storage:
    def __init__(self, filepath: str):
        self._filepath = Path(filepath)
        self._items = []

        if self._filepath.exists():
            self._load()

    def _load(self):
        with open(self._filepath, "r", encoding="utf-8") as f:
            raw_items = json.load(f)

        self._items = []
        for data in raw_items:
            task = Task.from_dict(data)
            self._items.append(task)

    def _save(self):
        with open(self._filepath, "w", encoding="utf-8") as f:
            data = [item.to_dict() for item in self._items]
            json.dump(data, f, ensure_ascii=False, indent=2)

    def add(self, item):
        self._items.append(item)
        self._save()

    def all(self):
        return list(self._items)