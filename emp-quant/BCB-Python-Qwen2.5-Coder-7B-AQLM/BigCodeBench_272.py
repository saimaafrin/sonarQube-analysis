
import cgi
import http.server
import json

def task_func():
    class JSONPostHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
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

            length = int(self.headers.get('Content-Length'))
            data = self.rfile.read(length)
            try:
                json_data = json.loads(data.decode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": "Invalid JSON data"
                }).encode('utf-8'))
                return

            if 'data' not in json_data:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({
                    "status": "error",
                    "message": "No data received"
                }).encode('utf-8'))
                return

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({
                "status": "success",
                "message": "Data received successfully."
            }).encode('utf-8'))

    return JSONPostHandler