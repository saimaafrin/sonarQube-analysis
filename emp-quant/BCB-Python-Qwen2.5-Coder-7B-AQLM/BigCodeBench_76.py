
import random
import string
from django.http import HttpResponse

def task_func(request, session_expire_time):
    def generate_session_key(length=20):
        if length != 20:
            raise ValueError("Session key length must be 20.")
        session_key = ''.join(random.choices(string.ascii_letters + string.digits, k=length))
        if not any(char.isdigit() for char in session_key) or not any(char.isalpha() for char in session_key):
            raise ValueError("Session key must contain both letters and digits.")
        return session_key

    try:
        session_key = generate_session_key()
        response = HttpResponse("Session key generated successfully.")
        response.set_cookie('session_key', session_key, max_age=session_expire_time)
        return response
    except ValueError as e:
        return HttpResponse(str(e), status=400)