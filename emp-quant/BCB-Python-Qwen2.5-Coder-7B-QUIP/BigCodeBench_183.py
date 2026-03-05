
from django.http import HttpResponse
import uuid

def task_func(data):
    # Generate a UUID for tracking
    request_id = uuid.uuid4()
    
    # Create a JSON response
    response_data = {
        'request_id': str(request_id),
        'data': data
    }
    
    # Create an HttpResponse with JSON data
    response = HttpResponse(response_data, content_type='application/json')
    
    # Add the UUID to the HTTP headers
    response['X-Request-ID'] = str(request_id)
    
    return response