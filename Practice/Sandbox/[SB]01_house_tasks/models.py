class HomeTask:
    def __init__(self, title, responsible):
        self.title = title
        self._responsible = responsible
        self._is_closed = False

    @property
    def is_closed(self):
        return self._is_closed

    @property
    def responsible(self):
        return self._responsible

    def __str__(self):
        return f"Task [{self.id}]: ({self.title} — for {self.responsible})"

    def __repr__(self):
        return f"Task [{self.id}]: {self.title}, for {self.responsible} was added"

    def close(self):
        if self._is_closed:
            raise ValueError ("Already closed")
        self._is_closed = True

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title,
            "responsible": self._responsible,
            "is_closed": self._is_closed
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(
            title = data["title"],
            responsible = data["responsible"]
        )
        task.id = data["id"]
        task._is_closed = data["is_closed"]
        return task


