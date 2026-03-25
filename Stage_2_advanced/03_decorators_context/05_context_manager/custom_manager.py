class FileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing file: {self.filename}")
        if self.file:
            self.file.close()

if __name__ == "__main__":
    with FileManager("custom.txt", "w") as f:
        f.write("Hello from custom context manager!\n")

    with FileManager("custom.txt", "r") as f:
        print("File content from custom manager:")
        print(f.read())