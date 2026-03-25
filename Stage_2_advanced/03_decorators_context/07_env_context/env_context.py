import os
from contextlib import contextmanager

@contextmanager
def change_dir(path):
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        print(f"Entered: {path}")
        yield
    finally:
        os.chdir(old_dir)
        print(f"Restored: {old_dir}")

if __name__ == "__main__":
    print("Before:", os.getcwd())
    with change_dir("/tmp"):
        print("Inside:", os.getcwd())
    print("After:", os.getcwd())