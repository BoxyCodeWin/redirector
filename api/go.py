import os
from http.server import BaseHTTPRequestHandler

class handler(BaseHTTPRequestHandler):
    def _redirect(self):
        dest = os.environ.get("DEST")
        if not dest:
            self.send_response(503); self.end_headers(); return
        self.send_response(302)
        self.send_header("Location", dest)
        self.send_header("Cache-Control", "no-store")
        self.end_headers()

    def do_GET(self):  self._redirect()
    def do_HEAD(self): self._redirect()
