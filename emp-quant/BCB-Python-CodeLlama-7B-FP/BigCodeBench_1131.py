import hashlib
import binascii
def task_func(salt, cursor):
    """
    Updates the passwords in a user table of an SQLite database by hashing them with SHA256, using a provided salt.
    The function directly modifies the database via the given cursor.
    The function should raise the exception for: TypeError if the salt is not a string
    The function should output with:
        int: The number of users whose passwords were successfully updated.
    """
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")

    # Update the password for each user in the database
    num_updated = 0
    for row in cursor.execute("SELECT * FROM users"):
        user_id = row["id"]
        password = row["password"]
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hashed_password, user_id))
        num_updated += 1

    return num_updated
salt = "my_salt"
cursor = None