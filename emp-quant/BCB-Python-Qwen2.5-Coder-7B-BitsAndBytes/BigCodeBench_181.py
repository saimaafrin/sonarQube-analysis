
from django.http import HttpResponse
from django.conf import settings
import random
import time

def task_func(data, min_delay, max_delay):
    # Generate a random delay between min_delay and max_delay
    delay = random.randint(min_delay, max_delay)
    
    # Simulate the delay
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    
    # Create JSON response data
    response_data = {
        'status': 'success',
        'message': 'Data processed after simulated delay',
        'data': data,
        'delay': delay
    }
    
    # Return HttpResponse with JSON data
    return HttpResponse(response_data, content_type='application/json')