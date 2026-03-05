import json
import random
import hashlib
from datetime import datetime
def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    # Check if utc_datetime is a datetime object
    if not isinstance(utc_datetime, datetime):
        raise ValueError("utc_datetime must be a datetime object")
    
    # Check if salt is a string
    if not isinstance(salt, str):
        raise ValueError("salt must be a string")
    
    # Generate a random lowercase alphanumeric password
    password = ''.join(random.choices('abcdefghijklmnopqrstuvwxyz0123456789', k=password_length))
    
    # Combine the password, salt, and UTC datetime string
    combined_string = password + salt + utc_datetime.strftime('%Y-%m-%d %H:%M:%S')
    
    # Hash the combined string using SHA-256
    hashed_password = hashlib.sha256(combined_string.encode()).hexdigest()
    
    # Encode the hashed password as a JSON string
    json_string = json.dumps(hashed_password)
    
    return json_string