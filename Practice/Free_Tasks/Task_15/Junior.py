note = input("Введите заметку: ")

file = open("notes.txt", "a")
file.write(note + "\n")
file.close()

file = open("notes.txt", "r")
lines = file.readlines()
file.close()

if len(lines) == 0:
    print("Нет заметок.")
else:
    print("Все заметки:")
    number = 1
    for line in lines:
        print(str(number) + ". " + line.strip())
        number += 1