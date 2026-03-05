import random
import string
from django.http import HttpResponse
def task_func(request, session_expire_time):
    # Generate a random session key of length 20
    session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=20))
    
    # Check if the session key contains both letters and digits
    if not (any(c.isalpha() for c in session_key) and any(c.isdigit() for c in session_key)):
        raise ValueError("Session key must contain both letters and digits.")
    
    # Set the session key in a cookie with the specified expiration time
    response = HttpResponse("Session key generated successfully.")
    response.set_cookie('session_key', session_key, max_age=session_expire_time)
    
    return response