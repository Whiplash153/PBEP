import os

print("=== OS Navigation ===\n")

start_dir = os.getcwd()
print("Start directory:", start_dir)

nested_path = os.path.join(start_dir, "demo_folder", "inner_folder")
os.makedirs(nested_path, exist_ok=True)
print("Nested folders created at:", nested_path)

os.chdir(nested_path)
print("Now inside:", os.getcwd())

with open ("test.txt", "w") as f:
    f.write("Hello from nested folder!")

print("File 'test.txt' created in:", os.getcwd())

os.chdir(start_dir)
print("Back to start directory:", os.getcwd())

print("\nContents of 'demo folder':", os.listdir("demo_folder"))

os.remove(os.path.join(nested_path, "test.txt"))
os.rmdir(nested_path)
os.rmdir(os.path.join(start_dir, "demo_folder"))
print("\nAll created folders and files removed.")

print("=== DONE ===")