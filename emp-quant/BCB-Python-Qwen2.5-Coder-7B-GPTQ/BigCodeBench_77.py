import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse
def task_func(data):
    try:
        # Check if required keys are present
        if 'username' not in data or 'password' not in data:
            raise KeyError("Missing required keys in input data.")
        
        # Decode the base64 password
        decoded_password = base64.b64decode(data['password'])
        
        # Generate the SHA-256 hash of the provided password
        provided_password_hash = hashlib.sha256(decoded_password).hexdigest()
        
        # Predefined correct password hash for demonstration
        correct_password_hash = hashlib.sha256('password'.encode()).hexdigest()
        
        # Authenticate the user
        if data['username'] == 'admin' and provided_password_hash == correct_password_hash:
            return HttpResponse('Login successful.', status=400)
        else:
            return HttpResponse('Login failed.', status=401)
    
    except (KeyError, UnicodeDecodeError, binascii.Error, ValueError) as e:
        return HttpResponseBadRequest(f'Bad Request: {str(e)}')
data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('wrongpassword'.encode()).digest()).decode()}