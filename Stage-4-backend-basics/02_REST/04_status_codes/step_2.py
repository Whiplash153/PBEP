def get_collection():

    items_exist = True

    if items_exist:
        return 200
    return 404

def get_item(item_exists):

    if item_exists:
        return 200
    return 404

print("Get /items:", get_collection())
print("Get /items/1 (exists):", get_item(True))
print("Get /items/2 (not exists):", get_item(False))