class SafeFileManager:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        print(f"[ENTER] Opening file: {self.filename}")
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()
            print(f"[EXIT] Closed file: {self.filename}")

        if exc_type:
            print(f"[ERROR] {exc_type.__name__}: {exc_val}")
            return True

if __name__ == "__main__":
    with SafeFileManager("safe.txt", "w") as f:
        f.write("This will work fine!\n")

    with SafeFileManager("safe.txt", "a") as f:
        f.write("Now something bad will happen...\n")
        1 / 0

    print("Chill, everything continues fine.")
