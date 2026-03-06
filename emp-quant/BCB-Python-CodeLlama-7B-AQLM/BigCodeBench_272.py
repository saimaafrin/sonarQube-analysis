import cgi
import http.server
import json
def task_func():
    """
    The function creates an HTTP POST request handler for processing incoming data. The data is expected to be in JSON format with a key 'data'. The handler responds with a 200 success message if the data is valid, or an error message otherwise.

    Notes:
    - If the 'Content-Type' header is not 'application/json', the server responds with a 400 Bad Request status and a JSON object:
      {"status": "error", "message": "Content-Type header is not application/json"}.
    - If the received JSON object does not contain a 'data' key, the response is a 400 Bad Request with a JSON object:
      {"status": "error", "message": "No data received"}.
    - For successfully processed requests, the server responds with a 200 OK status and a JSON object:
      {"status": "success", "message": "Data received successfully."}.

    Returns:
    class: A class that is a subclass of http.server.BaseHTTPRequestHandler, designed to handle HTTP POST requests.

    Requirements:
    - cgi
    - http.server
    - json

    Example:
    >>> handler = task_func()
    >>> server = http.server.HTTPServer(('127.0.0.1', 8080), handler)
    >>> server.serve_forever()
    """
    class Handler(http.server.BaseHTTPRequestHandler):
        def do_POST(self):
            if self.headers.get('Content-Type') != 'application/json':
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': 'Content-Type header is not application/json'}).encode('utf-8'))
                return

            length = int(self.headers.get('Content-Length'))
            data = self.rfile.read(length).decode('utf-8')
            try:
                data = json.loads(data)
            except json.JSONDecodeError:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': 'Invalid JSON data'}).encode('utf-8'))
                return

            if 'data' not in data:
                self.send_response(400)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'status': 'error', 'message': 'No data received'}).encode('utf-8'))
                return

            self.send_response(200)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()
            self.wfile.write(json.dumps({'status': 'success', 'message': 'Data received successfully.'}).encode('utf-8'))

    return Handler