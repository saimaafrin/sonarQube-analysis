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

    if username == 'admin' and password == base64.b64encode(hashlib.sha256('password'.encode()).digest()).decode():
        return HttpResponse('Login successful.', status=400)
    else:
        return HttpResponse('Login failed.', status=401)
data = {'username': 'admin', 'password': base64.b64encode(hashlib.sha256('password'.encode()).digest()).decode()}