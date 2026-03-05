from django.http import HttpResponse
import uuid
def task_func(data):
    # Generate a UUID
    request_id = str(uuid.uuid4())
    
    # Create JSON response data
    response_data = {
        'message': 'Data processed successfully',
        'data': data,
        'request_id': request_id
    }
    
    # Convert the response data to JSON format
    json_response = HttpResponse(response_data, content_type='application/json')
    
    # Add the UUID to the HTTP headers
    json_response['X-Request-ID'] = request_id
    
    return json_response