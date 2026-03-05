
import cgi
import http.server
import json

def task_func():
    class JSONPostHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            # Check if the Content-Type header is application/json
            if self.headers['Content-Type'] != 'application/json':
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "Content-Type header is not application/json"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                return

            # Read the length of the data
            content_length = int(self.headers['Content-Length'])
            # Read the data
            post_data = self.rfile.read(content_length)
            # Parse the JSON data
            try:
                data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "Invalid JSON"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                return

            # Check if 'data' key exists in the JSON object
            if 'data' not in data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "No data received"}
                self.wfile.write(json.dumps(response).encode('utf-8'))
                return

            # If all checks pass, send a success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "success", "message": "Data received successfully."}
            self.wfile.write(json.dumps(response).encode('utf-8'))

    return JSONPostHandler