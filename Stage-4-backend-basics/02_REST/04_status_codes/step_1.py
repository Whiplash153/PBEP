status_codes = {
    200: "OK",
    201: "Created",
    204: "No Content",
    400: "Bad Request",
    404: "Not Found",
    500: "Internal Server Error"
}

for code, meaning in status_codes.items():
    print(f"Status {code}: {meaning}")