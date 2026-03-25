from pathlib import Path

folder = Path("temp_data")
folder.mkdir(exist_ok=True)
print("Folder created:", folder.exists())

file = folder / "notes.txt"
file.write_text("Temporary file created for testing")
print("File created:", file.exists())

print("File content:", file.read_text())

if file.exists():
    file.unlink()
    print("File deleted:", not file.exists())

if folder.exists():
    folder.rmdir()
    print("Folder deleted:", not folder.exists())

