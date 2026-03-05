from django.http import HttpResponse
from django.conf import settings
import random
import time
def task_func(data, min_delay, max_delay):
    # Generate a random delay between min_delay and max_delay
    delay = random.randint(min_delay, max_delay)
    # Sleep for the generated delay
    time.sleep(delay)
    # Return a Django HttpResponse with JSON data
    return HttpResponse(data, content_type='application/json')
data = {'key': 'value'}
min_delay = 0
max_delay = 10