
from django.http import HttpResponse
import uuid

def task_func(data):
    # Generate a UUID for the request
    request_id = uuid.uuid4()

    # Create a JSON response with the data and the request ID
    response = HttpResponse(json.dumps(data), content_type='application/json')
    response['X-Request-ID'] = request_id

    return response