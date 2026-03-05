
import json
import random
import hashlib
from datetime import datetime

def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    if not isinstance(utc_datetime, datetime):
        raise ValueError("utc_datetime must be a datetime object")
    if not isinstance(salt, str):
        raise ValueError("salt must be a string")

    password = ''.join(random.choice('abcdefghijklmnopqrstuvwxyz0123456789') for _ in range(password_length))
    hashed_password = hashlib.sha256(f"{salt}{utc_datetime.isoformat()}".encode()).hexdigest()
    return json.dumps({"password": hashed_password})