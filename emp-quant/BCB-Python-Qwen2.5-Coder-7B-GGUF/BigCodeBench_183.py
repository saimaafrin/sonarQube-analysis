
from django.http import HttpResponse
import uuid

def task_func(data):
    # Convert data to JSON format
    json_data = json.dumps(data)
    
    # Generate a UUID
    request_uuid = str(uuid.uuid4())
    
    # Create HttpResponse with JSON data
    response = HttpResponse(json_data, content_type='application/json')
    
    # Add UUID to HTTP headers
    response['X-Request-ID'] = request_uuid
    
    return response