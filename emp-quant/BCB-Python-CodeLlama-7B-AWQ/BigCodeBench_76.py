import random
import string
from django.http import HttpResponse
def task_func(request, session_expire_time):
    """
    Generates a random session key comprising letters and digits with a specific length of 20, sets this key in a cookie on an HttpResponse object with the specified expiration time, and returns the HttpResponse object.
    """
    # Generate a random session key
    session_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

    # Set the session key in a cookie on the HttpResponse object
    response = HttpResponse()
    response.set_cookie('session_key', session_key, expires=session_expire_time)

    # Return the HttpResponse object
    return response