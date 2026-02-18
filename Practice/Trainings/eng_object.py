class Object:
    def __init__(self, author, title):
        self.author = author
        self.title = title
        self.is_closed = False

    def close_obj(self):
        if self.is_closed:
            raise ValueError("Already closed")
        self.is_closed = True