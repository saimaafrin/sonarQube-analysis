
import random
import string
from django.http import HttpResponse

def task_func(request, session_expire_time):
    def generate_session_key(length=20):
        characters = string.ascii_letters + string.digits
        while True:
            session_key = ''.join(random.choice(characters) for _ in range(length))
            if (any(c.isalpha() for c in session_key) and 
                any(c.isdigit() for c in session_key)):
                return session_key

    try:
        session_key = generate_session_key()
        response = HttpResponse("Session key generated successfully.")
        response.set_cookie('session_key', session_key, max_age=session_expire_time)
        return response
    except Exception as e:
        raise ValueError(f"Invalid session key: {e}")