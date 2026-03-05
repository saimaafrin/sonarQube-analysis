
import hashlib
import binascii

def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")
    
    # Hash the salt using SHA256
    salt_hash = hashlib.sha256(salt.encode()).hexdigest()
    
    # Update the passwords in the user table
    cursor.execute("UPDATE user SET password = ? WHERE password IS NOT NULL", (salt_hash,))
    
    # Get the number of rows affected
    rows_updated = cursor.rowcount
    
    return rows_updated