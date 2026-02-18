import os
from contextlib import contextmanager

@contextmanager
def safe_change_dir(path):
    old_dir = os.getcwd()
    try:
        os.chdir(path)
        print(f"Entered safely: {path}")
        yield os.getcwd()
    except Exception as e:
        print(f"Error caught: {e}")
    finally:
        os.chdir(old_dir)
        print(f"Restored safely: {old_dir}")

if __name__ == "__main__":
    print("Before:", os.getcwd())

    with safe_change_dir("/tmp") as p:
        print("Inside:", p)
        1 / 0

    print("After:", os.getcwd())


