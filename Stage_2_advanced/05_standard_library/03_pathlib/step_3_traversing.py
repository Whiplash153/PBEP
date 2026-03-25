from pathlib import Path

base_path = Path.cwd()

print("Current directory:", base_path)

print("\n--- Directory content ---")
for item in base_path.iterdir():
    print(item.name)

print("\n--- Python files ---")
for py_file in base_path.glob("*.py"):
    print(py_file.name)

print("\n--- All .txt files in project ---")
for txt_file in base_path.rglob("*.txt"):
    print(txt_file.relative_to(base_path))

print("\n--- MD files in project ---")
for md_file in base_path.rglob("*.md"):
    print(md_file.relative_to(base_path))