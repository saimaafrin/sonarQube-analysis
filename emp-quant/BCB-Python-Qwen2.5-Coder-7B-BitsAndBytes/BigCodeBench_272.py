
import cgi
import http.server
import json

class MyRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Check Content-Type header
        content_type = self.headers.get('Content-Type')
        if content_type != 'application/json':
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "error", "message": "Content-Type header is not application/json"}
            self.wfile.write(json.dumps(response).encode())
            return
        
        # Read the length of the data
        content_length = int(self.headers['Content-Length'])
        
        # Read the data
        post_data = self.rfile.read(content_length)
        
        try:
            # Parse the JSON data
            data = json.loads(post_data.decode('utf-8'))
            
            # Check if 'data' key exists
            if 'data' not in data:
                self.send_response(400)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                response = {"status": "error", "message": "No data received"}
                self.wfile.write(json.dumps(response).encode())
                return
            
            # Process the data (for demonstration, we'll just accept it)
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "success", "message": "Data received successfully."}
            self.wfile.write(json.dumps(response).encode())
        
        except json.JSONDecodeError:
            self.send_response(400)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            response = {"status": "error", "message": "Invalid JSON data"}
            self.wfile.write(json.dumps(response).encode())

def task_func():
    return MyRequestHandler