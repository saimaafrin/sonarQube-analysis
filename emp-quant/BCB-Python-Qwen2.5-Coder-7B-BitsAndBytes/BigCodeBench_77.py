
import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse

def task_func(data):
    try:
        # Check if required keys are present
        if 'username' not in data or 'password' not in data:
            raise KeyError("Missing keys in input data")
        
        # Decode the base64 encoded password
        decoded_password = base64.b64decode(data['password'])
        
        # Generate the SHA-256 hash of the provided password
        provided_hash = hashlib.sha256(decoded_password).hexdigest()
        
        # Predefined correct username and its corresponding hash
        correct_username = 'admin'
        correct_hash = hashlib.sha256('password'.encode()).hexdigest()
        
        # Authenticate the user
        if data['username'] == correct_username and provided_hash == correct_hash:
            return HttpResponse('Login successful.', status=400)
        else:
            return HttpResponse('Login failed.', status=401)
    
    except KeyError as e:
        return HttpResponseBadRequest(f"Key error: {e}")
    except UnicodeDecodeError:
        return HttpResponseBadRequest("Invalid base64 encoding")
    except binascii.Error:
        return HttpResponseBadRequest("Invalid base64 encoding")
    except ValueError:
        return HttpResponseBadRequest("Invalid input data")