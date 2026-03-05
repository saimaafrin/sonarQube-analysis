import json
import random
import hashlib
from datetime import datetime
def task_func(utc_datetime, salt='salt', password_length=10, seed=0):
    """
    Generate a random lowercase alphanumeric password of length password_length and then encrypt it as a JSON string.
    The password is hashed using SHA-256. The hashing uses the combination of the user provided salt and the complete conventional string representation of the user provided UTC datetime.
    The function should raise the exception for: ValueError: If the utc_datetime is not a datetime object or the salt is not a string.
    The function should output with:
        str: The hashed password encoded as a JSON string.
    """
    if not isinstance(utc_datetime, datetime):
        raise ValueError("utc_datetime must be a datetime object")
    if not isinstance(salt, str):
        raise ValueError("salt must be a string")

    # Generate a random lowercase alphanumeric password of length password_length
    password = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(password_length))

    # Hash the password using SHA-256
    hashed_password = hashlib.sha256(salt.encode() + str(utc_datetime).encode()).hexdigest()

    # Encode the hashed password as a JSON string
    json_password = json.dumps({"password": hashed_password})

    return json_password
utc_datetime = datetime.utcnow()
salt = "salt"
password_length = 10
seed = 0