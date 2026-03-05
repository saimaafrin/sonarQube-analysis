from django.http import HttpResponse
import uuid
def task_func(data):
    # Create a UUID for tracking requests
    uuid_str = str(uuid.uuid4())

    # Create a JSON response with the UUID
    response_data = {
        "uuid": uuid_str,
        "data": data
    }
    response = HttpResponse(json.dumps(response_data), content_type="application/json")

    # Add the UUID to the HTTP headers
    response["X-Request-ID"] = uuid_str

    return response
data = {"key": "value"}