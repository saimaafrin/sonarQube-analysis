
import cgi
import http.server
import json

class TaskHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_type = self.headers.get('Content-Type')
        if content_type != 'application/json':
            self.send_error(400, 'Content-Type header is not application/json')
            return

        try:
            data = json.loads(self.rfile.read(int(self.headers.get('Content-Length'))))
        except json.JSONDecodeError:
            self.send_error(400, 'Invalid JSON data')
            return

        if 'data' not in data:
            self.send_error(400, 'No data received')
            return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'success', 'message': 'Data received successfully.'}).encode('utf-8'))