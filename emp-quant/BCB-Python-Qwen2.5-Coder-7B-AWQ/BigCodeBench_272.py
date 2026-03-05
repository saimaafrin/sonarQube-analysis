import cgi
import http.server
import json
def task_func():
    class JSONPostHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            # Check if the content type is application/json
            if self.headers['Content-Type'] != 'application/json':
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "Content-Type header is not application/json"})
                self.wfile.write(response.encode('utf-8'))
                return

            # Read the data from the request
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            try:
                data = json.loads(post_data.decode('utf-8'))
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "Invalid JSON"})
                self.wfile.write(response.encode('utf-8'))
                return

            # Check if the 'data' key is present
            if 'data' not in data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "No data received"})
                self.wfile.write(response.encode('utf-8'))
                return

            # If all checks pass, send a success response
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "success", "message": "Data received successfully."})
            self.wfile.write(response.encode('utf-8'))

    return JSONPostHandler