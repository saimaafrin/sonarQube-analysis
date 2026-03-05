import cgi
import http.server
import json
def task_func():
    class JSONPostHandler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            # Check if the Content-Type header is 'application/json'
            content_type = self.headers.get('Content-Type')
            if content_type != 'application/json':
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "Content-Type header is not application/json"})
                self.wfile.write(response.encode('utf-8'))
                return

            # Read the incoming data
            length = int(self.headers['Content-Length'])
            data = self.rfile.read(length)
            try:
                json_data = json.loads(data)
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "Invalid JSON"})
                self.wfile.write(response.encode('utf-8'))
                return

            # Check if the 'data' key is present in the JSON object
            if 'data' not in json_data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = json.dumps({"status": "error", "message": "No data received"})
                self.wfile.write(response.encode('utf-8'))
                return

            # If all checks pass, respond with success
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = json.dumps({"status": "success", "message": "Data received successfully."})
            self.wfile.write(response.encode('utf-8'))

    return JSONPostHandler