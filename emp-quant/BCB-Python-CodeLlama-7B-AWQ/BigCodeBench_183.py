from django.http import HttpResponse
import uuid
def task_func(data):
    """
    Create a Django HttpResponse with JSON data and UUID in the HTTP headers to track requests.
    """
    response = HttpResponse(data, content_type='application/json')
    response['X-Request-ID'] = str(uuid.uuid4())
    return response
data = {'key': 'value'}