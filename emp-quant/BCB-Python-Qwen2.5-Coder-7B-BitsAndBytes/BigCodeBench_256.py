
import json
import random
import hashlib
from datetime import datetime

def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    if not isinstance(utc_datetime, datetime):
        raise ValueError("utc_datetime must be a datetime object")
    if not isinstance(salt, str):
        raise ValueError("salt must be a string")

    # Generate a random lowercase alphanumeric password
    characters = 'abcdefghijklmnopqrstuvwxyz0123456789'
    password = ''.join(random.choice(characters) for _ in range(password_length))

    # Combine the password, salt, and UTC datetime to create a hash input
    hash_input = f"{password}{salt}{utc_datetime.isoformat()}"

    # Hash the combined string using SHA-256
    hasher = hashlib.sha256()
    hasher.update(hash_input.encode('utf-8'))
    hashed_password = hasher.hexdigest()

    # Create a dictionary to store the hashed password
    result_dict = {
        "hashed_password": hashed_password,
        "original_password": password
    }

    # Convert the dictionary to a JSON string
    result_json = json.dumps(result_dict)

    return result_json