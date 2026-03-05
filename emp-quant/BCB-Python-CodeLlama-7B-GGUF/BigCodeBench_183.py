
from django.http import HttpResponse
import uuid

def task_func(data):
    # Generate a UUID for tracking requests
    request_id = uuid.uuid4()

    # Create a JSON response with the UUID
    response_data = {
        'request_id': request_id,
        'data': data
    }
    response = HttpResponse(json.dumps(response_data), content_type='application/json')

    # Add the UUID to the HTTP headers
    response['X-Request-ID'] = request_id

    return response