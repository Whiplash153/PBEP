def make_list(data):
    result = []
    for name, info in data.items():
        item = StoreItem(name, info["price"], info["qty"])
        result.append(item)
    return result


