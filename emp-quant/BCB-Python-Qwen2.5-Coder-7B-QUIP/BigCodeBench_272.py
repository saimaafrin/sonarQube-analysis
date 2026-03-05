
import cgi
import http.server
import json

def task_func():
    class PostHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            # Check Content-Type header
            content_type = self.headers.get('Content-Type')
            if content_type != 'application/json':
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": "Content-Type header is not application/json"
                }).encode('utf-8'))
                return

            # Parse JSON data
            try:
                length = int(self.headers['Content-Length'])
                data = self.rfile.read(length)
                data = json.loads(data.decode('utf-8'))
            except (ValueError, KeyError):
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": "No data received"
                }).encode('utf-8'))
                return

            # Check if 'data' key exists
            if 'data' not in data:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": "No data received"
                }).encode('utf-8'))
                return

            # Respond with success
            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "success",
                "message": "Data received successfully."
            }).encode('utf-8'))

    return PostHandler