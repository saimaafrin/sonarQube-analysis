
import cgi
import http.server
import json

class TaskHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Check if the Content-Type header is application/json
        if self.headers.get('Content-Type') != 'application/json':
            self.send_error(400, 'Content-Type header is not application/json')
            return

        # Read the JSON data from the request body
        data = json.loads(self.rfile.read(int(self.headers['Content-Length'])))

        # Check if the JSON data contains a 'data' key
        if 'data' not in data:
            self.send_error(400, 'No data received')
            return

        # Process the data and respond with a 200 OK status
        self.send_response(200)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({'status': 'success', 'message': 'Data received successfully.'}).encode('utf-8'))