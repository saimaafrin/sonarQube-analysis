
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
    if username == 'admin' and password == hashlib.sha256(password.encode()).digest():
        return HttpResponse('Login successful.')
    else:
        return HttpResponse('Login failed.', status=401)