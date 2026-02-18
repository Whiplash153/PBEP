method = "POST"
data_is_valid = True
item_exists = False

if method == "POST":
    if not data_is_valid:
        status_code = 400
    else:
        status_code = 201

elif method == "PUT":
    if not data_is_valid:
        status_code = 400
    elif not item_exists:
        status_code = 404
    else:
        status_code = 200

elif method == "PATCH":
    if not data_is_valid:
        status_code = 400
    elif not item_exists:
        status_code = 404
    else:
        status_code = 200

print("Status code:", status_code)