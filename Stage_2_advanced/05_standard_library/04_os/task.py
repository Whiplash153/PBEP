import os

print("Start task\n")

current_folder = os.getcwd()
print("Current folder:", current_folder)

new_folder_name = "system_test"
if not os.path.exists(new_folder_name):
    os.mkdir(new_folder_name)
    print(f"Folder '{new_folder_name}' created")
else:
    print(f"Folder '{new_folder_name}' already exists")
os.chdir(new_folder_name)

with open("test.txt", "w") as f:
    user_environ = os.environ.get("USER", "unknown")
    f.write(f"Current user: {user_environ}")

print("Now in:", os.getcwd())

os.chdir(current_folder)
print("Moved back to:", os.getcwd())

os.remove(os.path.join(new_folder_name, "test.txt"))
os.rmdir(new_folder_name)

print("Path preview:", os.environ.get("PATH", "")[:100])

print("\nDone")


