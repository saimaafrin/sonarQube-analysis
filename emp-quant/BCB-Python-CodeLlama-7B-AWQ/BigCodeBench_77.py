import hashlib
import base64
import binascii
from django.http import HttpResponseBadRequest, HttpResponse
def task_func(data):
    try:
        username = data['username']
        password = data['password']
    except KeyError:
        return HttpResponseBadRequest('Bad Request.')

    if username != 'admin':
        return HttpResponseBadRequest('Bad Request.')

    try:
        password_hash = base64.b64decode(password)
    except UnicodeDecodeError:
        return HttpResponseBadRequest('Bad Request.')

    if hashlib.sha256(password_hash).hexdigest() != 'password':
        return HttpResponseBadRequest('Bad Request.')

    return HttpResponse('Login successful.', status=400)
data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('wrongpassword'.encode()).digest()).decode()}