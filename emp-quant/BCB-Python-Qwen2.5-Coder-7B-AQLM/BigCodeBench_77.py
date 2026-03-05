
import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse

def task_func(data):
    try:
        # Check if the required keys are present
        if 'username' not in data or 'password' not in data:
            raise KeyError("Missing keys in input data")
        
        # Decode the base64 encoded password
        decoded_password = base64.b64decode(data['password'])
        
        # Generate the SHA-256 hash of the password
        password_hash = hashlib.sha256(decoded_password).hexdigest()
        
        # Predefined correct username and password hash for demonstration
        correct_username = 'admin'
        correct_password_hash = hashlib.sha256('password'.encode()).hexdigest()
        
        # Authenticate the credentials
        if data['username'] == correct_username and password_hash == correct_password_hash:
            return HttpResponse('Login successful.', status=400)
        else:
            return HttpResponse('Login failed.', status=401)
    
    except KeyError:
        return HttpResponseBadRequest('Bad Request.')
    except UnicodeDecodeError:
        return HttpResponseBadRequest('Bad Request.')
    except binascii.Error:
        return HttpResponseBadRequest('Bad Request.')
    except ValueError:
        return HttpResponseBadRequest('Bad Request.')