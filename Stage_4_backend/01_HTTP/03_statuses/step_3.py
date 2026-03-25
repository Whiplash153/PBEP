print("=== SUCCESS ===")
action = "read"
error = "server"

if error == "client":
    print("400 — Client error: invalid request data")
elif error == "server":
    print("500 — Server error: something crashed")
else:
    if action == "create":
        print("201 — Created")
    elif action == "read":
        print("200 — OK")
    elif action == "update":
        print("204 — No content (update successful)")
    elif action == "delete":
        print("204 — No content (delete successful)")