
from django.http import HttpResponse
from django.conf import settings
import random
import time

def task_func(data, min_delay, max_delay):
    # Generate a random delay between min_delay and max_delay
    delay = random.uniform(min_delay, max_delay)
    # Sleep for the generated delay
    time.sleep(delay)
    # Create a JSON response with the data
    response_data = {
        "message": "Task completed",
        "data": data
    }
    # Return the HttpResponse with the JSON data
    return HttpResponse(response_data, content_type="application/json")