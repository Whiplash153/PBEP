from safe_manager import SafeFileManager

with SafeFileManager("report.txt", "w") as f:
    f.write("We are good")
    1 / 0

with SafeFileManager("report.txt", "r") as f:
    print("Content inside:")
    print(f.read())
