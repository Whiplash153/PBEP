from pathlib import Path

folder = Path("project_data")
folder.mkdir(exist_ok=True)
print("Folder project_data created:", folder.exists())

for name in ["notex.txt", "report.txt", "summary.txt"]:
    file = folder / name
    file.write_text("Created by pathlib")
    print(f"File {name} created", file.exists())

print("\n=== Total .txt files in folder ===")
txt_files = list(folder.glob("*.txt"))
for txt_file in txt_files:
    print(txt_file.relative_to(folder))

print(f"\nTotal .txt files: {len(txt_files)}")

for txt_file in folder.glob("*.txt"):
    txt_file.unlink()

print("\nAll .txt files deleted")

if folder.exists():
    folder.rmdir()
    print("Folder deleted:", not folder.exists())
