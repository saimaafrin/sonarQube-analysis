import hashlib
import binascii
def task_func(salt, cursor):
    """
    Updates the passwords in a user table of an SQLite database by hashing them with SHA256, using a provided salt.
    The function directly modifies the database via the given cursor.
    The function should raise the exception for:
        TypeError if the salt is not a string
    The function should output with:
        int: The number of users whose passwords were successfully updated.
    """
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")

    # Update the password hashes in the user table
    cursor.execute("UPDATE user SET password = ? WHERE password IS NOT NULL", (hashlib.sha256(salt.encode() + password.encode()).hexdigest(),))

    # Get the number of rows affected
    num_rows = cursor.rowcount

    return num_rows