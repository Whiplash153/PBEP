note = input("Add new note:")

def add_note(text):
    with open("notes.txt", "a", encoding="utf-8") as f:
        f.write(text + "\n")

def show_notes():
    with open("notes.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        if not lines:
            print("No notes yet.")
            return
        for i, line in enumerate(lines, start=1):
            print(f"{i}. {line.strip()}")

add_note(note)

print("All notes:")
show_notes()
