open("notes.txt", "w").close()

def add_note(text):
    with open("notes.txt", "a") as f:
        f.write(text + "\n")

def show_notes():
    with open("notes.txt", "r") as f:
        for line in f:
            print(line.strip())

add_note("First note")
add_note("Second note")

print("All notes:")
show_notes()