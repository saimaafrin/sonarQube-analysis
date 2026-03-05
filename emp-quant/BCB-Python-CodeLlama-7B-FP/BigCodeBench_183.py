from django.http import HttpResponse
import uuid
def task_func(data):
    """
    Create a Django HttpResponse with JSON data and UUID.
    """
    # Generate a UUID for tracking requests
    uuid_str = str(uuid.uuid4())

    # Create a JSON response with the UUID
    response_data = {
        "uuid": uuid_str,
        "data": data,
    }
    response = HttpResponse(
        content_type="application/json",
        json_data=response_data,
    )

    # Add the UUID to the HTTP headers
    response["X-Request-ID"] = uuid_str

    return response
data = {"key": "value"}