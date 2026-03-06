
import random
import string
from django.http import HttpResponse

def task_func(request, session_expire_time):
    # Generate a random session key
    session_key = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(20))

    # Set the session key in a cookie
    response = HttpResponse("Session key generated successfully.")
    response.set_cookie(
        "session_key",
        session_key,
        expires=session_expire_time,
        secure=True,
        httponly=True,
    )

    return response