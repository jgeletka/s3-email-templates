#!/usr/bin/env python3
import http.server, socketserver, os, sys

PORT = int(os.environ.get("PORT", 3030))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class Handler(http.server.SimpleHTTPRequestHandler):
    def log_message(self, fmt, *args):
        pass  # silent

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    httpd.serve_forever()
