#!/usr/bin/python3
"""
restful-api.task_03_http_server
"""
import json
import http.server


class Handler(http.server.BaseHTTPRequestHandler):
    """
    Handler
    """

    def do_GET(self):
        """
        do_GET
        """
        j = json.dumps({"name": "John", "age": 30, "city": "New York"})
        i = json.dumps({"version": "1.0", "description":
                        "A simple API built with http.server"})
        if self.path == "/":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        elif self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(j.encode("utf-8"))

        elif self.path == "/status":
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        elif self.path == "/info":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            self.wfile.write(i.encode("utf-8"))

        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"404 Not Found")


if __name__ == "__main__":
    server = http.server.HTTPServer(("", 8000), Handler)
    server.serve_forever()
