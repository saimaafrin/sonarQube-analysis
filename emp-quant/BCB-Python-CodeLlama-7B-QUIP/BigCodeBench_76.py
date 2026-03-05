
import random
import string
from django.http import HttpResponse

def task_func(request, session_expire_time):
    # Generate a random session key
    session_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

    # Set the session key in a cookie
    response = HttpResponse(status=200)
    response.set_cookie('session_key', session_key, expires=session_expire_time)

    # Check if the session key contains both letters and digits
    if not (session_key.isalpha() or session_key.isdigit()):
        raise ValueError("Session key must contain both letters and digits")

    # Check if the session key length is equal to 20
    if len(session_key) != 20:
        raise ValueError("Session key length must be equal to 20")

    # Set the response content
    response.content = "Session key generated successfully."

    return response