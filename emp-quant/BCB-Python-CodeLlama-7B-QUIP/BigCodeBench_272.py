
import cgi
import http.server
import json

class TaskHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        # Get the JSON data from the request
        try:
            data = json.loads(self.rfile.read(1024))
        except ValueError:
            self.send_error(400, "Bad Request")
            return

        # Check if the data has a 'data' key
        if 'data' not in data:
            self.send_error(400, "Bad Request")
            return

        # Process the data
        # ...

        # Respond with a 200 OK status
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps({"status": "success", "message": "Data received successfully."}))