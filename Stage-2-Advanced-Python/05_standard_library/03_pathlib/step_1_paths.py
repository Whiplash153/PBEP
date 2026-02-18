from pathlib import Path

current = Path.cwd()
print("Current directory:", current)

new_folder = current / "example_folder"
new_file = new_folder / "data.txt"
print("New folder:", new_folder)
print("New file:", new_file)

print("Does folder exist?", new_folder.exists())
print("Does file exist?", new_file.exists())

print("Is directory?", new_folder.is_dir())
print("Is file?", new_file.is_dir())