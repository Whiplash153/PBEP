file = open("example.txt", "w")
file.write("Hello from manual file handling!\n")
file.close()

with open("example.txt", "a") as file:
    file.write("Hello from context manager!\n")

with open("example.txt", "r") as file:
    print("File content:")
    print(file.read())