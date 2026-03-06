
import hashlib
import binascii

def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")

    # Update the passwords in the user table
    cursor.execute("UPDATE user SET password = ? WHERE password IS NOT NULL", (hashlib.sha256(salt.encode() + password.encode()).hexdigest(),))

    # Get the number of rows affected
    num_rows = cursor.rowcount

    # Return the number of users whose passwords were successfully updated
    return num_rows