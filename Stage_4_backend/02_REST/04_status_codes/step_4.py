# HTTP status codes cheat sheet:
# 200 OK                    -> request succeeded
# 201 Created               -> resource was created
# 204 No Content            -> request succeeded, no response body
# 400 Bad Request           -> invalid request data
# 404 Not Found             -> resource does not exist
# 500 Internal Server Error -> not your fault

method = "DELETE"        # GET, POST, PUT, PATCH, DELETE
data_is_valid = True
item_exists = True

if method == "GET":
    if item_exists:
        status_code = 200
    else:
        status_code = 404

elif method == "POST":
    if not data_is_valid:
        status_code = 400
    else:
        status_code = 201

elif method == "PUT" or method == "PATCH":
    if not data_is_valid:
        status_code = 400
    elif not item_exists:
        status_code = 404
    else:
        status_code = 200

elif method == "DELETE":
    if not item_exists:
        status_code = 404
    else:
        status_code = 204

print("Status code:", status_code)