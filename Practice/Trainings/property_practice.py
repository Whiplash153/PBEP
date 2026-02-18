class Task:
    def __init__(self):
        self._is_closed = False

    @property
    def is_closed(self):
        return self._is_closed

    @is_closed.setter
    def is_closed(self, value):
        if not isinstance(value, bool):
            raise ValueError("must be True or False")
        self._is_closed = value

    def close(self):
        self._is_closed = True

task = Task()
print("Before:", task.is_closed)

task.close()
print("After close:", task.is_closed)

task.is_closed = False
print("After hack:", task.is_closed)