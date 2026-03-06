
from django.http import HttpResponse
from django.conf import settings
import random
import time

def task_func(data, min_delay, max_delay):
    # Generate a random delay between min_delay and max_delay
    delay = random.randint(min_delay, max_delay)
    time.sleep(delay)

    # Create a JSON response with the data
    response = HttpResponse(data, content_type='application/json')

    # Add a delay header to the response
    response['X-Delay'] = str(delay)

    return response