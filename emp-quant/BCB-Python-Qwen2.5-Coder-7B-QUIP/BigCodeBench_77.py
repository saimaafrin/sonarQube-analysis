
import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse

def task_func(data):
    try:
        # Check if the required keys are present
        if 'username' not in data or 'password' not in data:
            raise ValueError("Missing required keys")

        # Decode the password from base64
        password_hash = base64.b64decode(data['password'])

        # Calculate the SHA-256 hash of the password
        expected_hash = base64.b64encode(hashlib.sha256('password'.encode()).digest())

        # Compare the hashes
        if password_hash == expected_hash:
            return HttpResponse("Login successful.", status=400)
        else:
            return HttpResponse("Login failed.", status=401)
    except (KeyError, UnicodeDecodeError, binascii.Error, ValueError) as e:
        return HttpResponseBadRequest("Bad Request")