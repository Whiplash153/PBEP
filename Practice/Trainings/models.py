class Task:
    def __init__(self, title, id):
        self.id = id
        self.title = title

    def to_dict(self):
        return {
            "id": self.id,
            "title": self.title
        }
    @classmethod
    def from_dict(cls, data):
        return cls(
            id = data["id"],
            title = data["title"]
        )