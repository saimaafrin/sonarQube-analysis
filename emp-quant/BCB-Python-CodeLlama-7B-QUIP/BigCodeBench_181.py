
from django.http import HttpResponse
from django.conf import settings
import random
import time

def task_func(data, min_delay, max_delay):
    delay = random.randint(min_delay, max_delay)
    time.sleep(delay)
    return HttpResponse(data)