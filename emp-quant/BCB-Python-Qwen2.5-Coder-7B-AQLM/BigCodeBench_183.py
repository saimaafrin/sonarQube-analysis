
from django.http import HttpResponse
import uuid

def task_func(data):
    # Generate a UUID
    request_id = uuid.uuid4()
    
    # Convert data to JSON
    json_data = json.dumps(data)
    
    # Create HttpResponse with JSON data
    response = HttpResponse(json_data, content_type='application/json')
    
    # Add UUID to HTTP headers
    response['X-Request-ID'] = str(request_id)
    
    return response