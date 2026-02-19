items = {}
next_id = 1

def get_all_items():
    return list(items.values())

def get_item(item_id):
    return items.get(item_id)

def create_item(data):
    global next_id

    item = {
        "id": next_id,
        "name": data.get("name")
    }

    items[next_id] = item
    next_id += 1

    return item

def delete_item(item_id):
    return items.pop(item_id, None)