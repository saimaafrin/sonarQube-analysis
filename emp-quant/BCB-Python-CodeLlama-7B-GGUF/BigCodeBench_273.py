
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

class TaskHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        content_type = self.headers.get('Content-Type')
        if content_type != 'application/json':
            self.send_response(400)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Content-Type header is not application/json')
            return

        length = int(self.headers.get('Content-Length'))
        data = self.rfile.read(length).decode('utf-8')
        try:
            json_data = json.loads(data)
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Invalid JSON')
            return

        if 'data' not in json_data:
            self.send_response(400)
            self.send_header('Content-Type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'No data key in request')
            return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(SUCCESS_RESPONSE).encode('utf-8'))