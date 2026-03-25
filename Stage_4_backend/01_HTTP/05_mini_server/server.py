from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):

    def do_GET(self):

        print("Method:", self.command)
        print("Path:", self.path)

        print("Headers:")
        for key, value in self.headers.items():
            print(f"{key}: {value}")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Server received your request")
        self.log_request_data("GET", self.path, self.headers)

    def do_POST(self):
        print("Method:", self.command)
        print("Path:", self.path)

        print("Headers:")
        for key, value in self.headers.items():
            print(f"{key}: {value}")

        content_length = int(self.headers.get("Content-Length", 0))
        body = self.rfile.read(content_length)
        print("Body:", body.decode("utf-8"))

        self.send_response(200)
        self.send_header("Content-Type", "text/plain")
        self.end_headers()
        self.wfile.write(b"POST request received")
        self.log_request_data("POST", self.path, self.headers, body.decode("utf-8"))

    def log_request_data(self, method, path, headers, body=None):
        with open("requests.log", "a", encoding="utf-8") as f:
            f.write(f"Method: {method}\n")
            f.write(f"Path: {path}\n")
            f.write("Headers:\n")
            for key, value in headers.items():
                f.write(f" {key}: {value}\n")
            if body:
                f.write(f"Body: {body}\n")
            f.write(("\n---\n\n"))

def run():
    server = HTTPServer(("localhost", 8000), SimpleHandler)
    print("Server running at http://localhost:8000")
    server.serve_forever()

if __name__ == "__main__":
    run()