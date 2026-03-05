from django.http import HttpResponse
from django.conf import settings
import random
import time
def task_func(data, min_delay, max_delay):
    """
    Generate a Django HttpResponse with JSON data to simulate the latency of the network.
    """
    # Generate a random delay between min_delay and max_delay
    delay = random.uniform(min_delay, max_delay)
    time.sleep(delay)

    # Create a Django HttpResponse with JSON data
    response = HttpResponse(data, content_type='application/json')

    return response
data = {'key1': 'value1', 'key2': 'value2'}
min_delay = 0.1
max_delay = 1