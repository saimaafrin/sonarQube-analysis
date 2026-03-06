
from django.http import HttpResponse
import uuid

def task_func(data):
    # Convert the data dictionary to a JSON string
    json_data = json.dumps(data)
    
    # Generate a UUID for tracking the request
    request_uuid = str(uuid.uuid4())
    
    # Create an HttpResponse object with the JSON data
    response = HttpResponse(json_data, content_type='application/json')
    
    # Add the UUID to the HTTP headers
    response['X-Request-ID'] = request_uuid
    
    return response