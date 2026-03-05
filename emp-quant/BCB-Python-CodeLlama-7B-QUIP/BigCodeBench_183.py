
from django.http import HttpResponse
import uuid

def task_func(data):
    # Create a UUID for the request
    request_uuid = uuid.uuid4()

    # Create a Django HttpResponse with JSON data
    response = HttpResponse(data, content_type='application/json')

    # Add the UUID to the HTTP headers
    response['X-Request-Id'] = request_uuid

    return response