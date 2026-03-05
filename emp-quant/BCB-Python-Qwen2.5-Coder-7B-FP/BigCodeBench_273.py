import cgi
import http.server
import json
SUCCESS_RESPONSE = {
    'status': 'success',
    'message': 'Data received successfully.'
}
class JSONDataHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        content_type = self.headers['Content-Type']
        if content_type != 'application/json':
            self.send_error(400, 'Content-Type header is not application/json')
            return

        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        try:
            data = json.loads(post_data)
        except json.JSONDecodeError:
            self.send_error(400, 'Invalid JSON')
            return

        if 'data' not in data:
            self.send_error(400, 'No data key in request')
            return

        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps(SUCCESS_RESPONSE).encode('utf-8'))
def task_func():
    return JSONDataHandler