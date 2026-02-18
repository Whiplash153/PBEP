import os
from os import chdir


class ChangeDir:
    def __init__(self, new_path):
        self.new_path = new_path
        self.old_path = None

    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.new_path)
        print(f"Entered: {self.new_path}")
        return  os.getcwd()

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_path)
        print(f"Restored: {self.old_path}")

if __name__ == "__main__":
    print("Before:", os.getcwd())
    with ChangeDir("/tmp"):
        print("Inside:", os.getcwd())
    print("After:", os.getcwd())

