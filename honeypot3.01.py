import socketserver
import http.server
import os

PORT = 80
FILE = "D:\important folders\/very important\exp.txt"

class FakeFileHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        if path.endswith(FILE):
            return FILE
        return http.server.SimpleHTTPRequestHandler.translate_path(self, path)

httpd = socketserver.TCPServer(("", PORT), FakeFileHandler)

print("Fake file honeypot is running on port", PORT)

httpd.serve_forever()
