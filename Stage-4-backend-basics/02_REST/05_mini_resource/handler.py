from storage import (
    get_all_items,
    get_item,
    create_item,
    delete_item
)

def handle_request(method, path, data=None):
    response = None

    # --- rounting ---
    parts = path.strip("/").split("/")

    if parts[0] != "items":
        return 404, None

    is_collection = len(parts) == 1
    is_item = len(parts) == 2

    item_id = None
    if is_item:
        try:
            item_id = int(parts[1])
        except ValueError:
            return 400, None

    # --- GET ---
    if method == "GET":
        if is_collection:
            response = get_all_items()
            return 200, response

        item = get_item(item_id)
        if item is None:
            return 404, None

        return 200, item

    # --- POST ---
    if method == "POST":
        if not is_collection:
            return 400, None

        if not data or "name" not in data:
            return 400, None

        item = create_item(data)
        return 201, item

    # --- PUT ---
    if method == "PUT":
        if not is_item:
            return 400, None

        if not data or "name" not in data:
            return 400, None

        item = get_item(item_id)
        if item is None:
            return 404, None

        item["name"] = data["name"]
        return 200, item

    # --- DELETE ---
    if method == "DELETE":
        if not is_item:
            return 400, None

        deleted = delete_item(item_id)
        if deleted is None:
            return 404, None

        return 204, None

    return  405, None