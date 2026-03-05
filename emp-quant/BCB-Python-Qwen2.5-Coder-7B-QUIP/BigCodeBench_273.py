
import cgi
import http.server
import json
SUCCESS_RESPONSE = {
    'status': 'success',
    'message': 'Data received successfully.'
}
ERROR_RESPONSE = {
    'status': 'error',
    'message': 'Invalid data received.'
}

class TaskHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_type = self.headers.get_content_type()
        if content_type != 'application/json':
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "error", "message": "Content-Type header is not application/json"}')
            return

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)

        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "error", "message": "Invalid JSON"}')
            return

        if 'data' not in data:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "error", "message": "No data key in request"}')
            return

        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(b'{"status": "success", "message": "Data received successfully."}')

def task_func():
    return TaskHandler