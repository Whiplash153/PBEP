from handler import handle_request


def demo(method, path, data=None):
    status, response = handle_request(method, path, data)
    print(f"{method} {path} -> {status}, response: {response}")


# --- GET empty collection ---
demo("GET", "/items")

# --- CREATE items ---
demo("POST", "/items", {"name": "Apple"})
demo("POST", "/items", {"name": "Banana"})

# --- GET collection ---
demo("GET", "/items")

# --- GET single item ---
demo("GET", "/items/1")
demo("GET", "/items/999")

# --- UPDATE item ---
demo("PUT", "/items/1", {"name": "Green Apple"})
demo("PUT", "/items/999", {"name": "Ghost"})

# --- DELETE item ---
demo("DELETE", "/items/1")
demo("DELETE", "/items/1")

# --- INVALID requests ---
demo("POST", "/items/1", {"name": "Wrong"})
demo("PUT", "/items", {"name": "Wrong"})
demo("GET", "/unknown")