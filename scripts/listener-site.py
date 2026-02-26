#!/usr/bin/env python3
"""Minimal static file server for KXST listener page with API proxy."""
import http.server
import os
import urllib.request
import json

PORT = 8090
DIRECTORY = os.path.expanduser("~/kxst/docs/listener")

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

    def do_GET(self):
        # Proxy /api/* to LibreTime on localhost:8080
        if self.path.startswith('/api/'):
            try:
                url = 'http://localhost:8080' + self.path
                with urllib.request.urlopen(url, timeout=5) as resp:
                    data = resp.read()
                    self.send_response(200)
                    self.send_header('Content-Type', 'application/json')
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(data)
            except Exception:
                self.send_response(502)
                self.end_headers()
            return
        super().do_GET()

if __name__ == '__main__':
    server = http.server.HTTPServer(('127.0.0.1', PORT), Handler)
    print(f"Serving {DIRECTORY} on port {PORT}")
    server.serve_forever()
