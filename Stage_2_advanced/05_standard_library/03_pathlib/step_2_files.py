from pathlib import Path

file_path = Path("example.txt")

file_path.write_text("Hello from pathlib!\nThis file was created with Path objects.")
print("File created and written successfully.")

print("File exists:", file_path.exists())

content = file_path.read_text()
print("File content:")
print(content)