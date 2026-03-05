
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

def task_func():
    def handle_post(request):
        content_type = request.headers.get('Content-Type')
        if content_type != 'application/json':
            return http.server.HTTPError(400, "Content-Type header is not application/json")
        try:
            data = json.loads(request.body)
        except json.JSONDecodeError:
            return http.server.HTTPError(400, "Invalid JSON")
        if 'data' not in data:
            return http.server.HTTPError(400, "No data key in request")
        return SUCCESS_RESPONSE
    return handle_post