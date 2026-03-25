import os

print("=== OS Overview ===\n")

print("OS name:", os.name)

print("Current working directory:", os.getcwd())

folder_name = "os_demo"
if not os.path.exists(folder_name):
    os.mkdir(folder_name)
    print(f"Folder '{folder_name}' created.")
else:
    print(f"Folder '{folder_name}' already exists.")

print("\nCurrent directory contents:")
print(os.listdir())

os.rmdir(folder_name)
print(f"\nFolder '{folder_name}' removed.")

print("\n=== DONE ===")