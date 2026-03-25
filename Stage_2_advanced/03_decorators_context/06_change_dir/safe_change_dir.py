import os

class SafeChangeDir:
    def __init__(self, new_path):
        self.new_path = new_path
        self.old_path = None

    def __enter__(self):
        self.old_path = os.getcwd()
        os.chdir(self.new_path)
        print(f"Entered safely:, {self.new_path}")
        return os.getcwd()

    def __exit__(self, exc_type, exc_val, exc_tb):
        os.chdir(self.old_path)
        print(f"Restored safely: {self.old_path}")

        if exc_type:
            print(f"Error caught: {exc_type.__name__} - {exc_val}")
            return True

if __name__ == "__main__":
    print("Before safe test:", os.getcwd())
    with SafeChangeDir("/tmp") as p:
        print("Inside safe test:", p)
        1 / 0
    print("After safe test:", os.getcwd())
