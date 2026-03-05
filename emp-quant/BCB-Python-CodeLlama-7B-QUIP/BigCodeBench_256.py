
import json
import random
import hashlib
from datetime import datetime

def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    if not isinstance(utc_datetime, datetime):
        raise ValueError('utc_datetime must be a datetime object')
    if not isinstance(salt, str):
        raise ValueError('salt must be a string')
    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz') for _ in range(password_length))
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return json.dumps({'hashed_password': hashed_password, 'salt': salt, 'utc_datetime': utc_datetime.isoformat()})