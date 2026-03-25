with open("data.txt", "w") as f:
    f.write("First line\n")
    f.write("Second line\n")

with open("data.txt", "r") as f:
    content = f.read()

print("File content:")
print(content)