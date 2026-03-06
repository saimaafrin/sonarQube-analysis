
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

    try:
        password_hash = base64.b64decode(password)
    except binascii.Error:
        return HttpResponseBadRequest('Bad Request.')

    if username == 'admin' and hashlib.sha256(password_hash).hexdigest() == 'password':
        return HttpResponse('Login successful.', status=400)
    else:
        return HttpResponse('Login failed.', status=401)