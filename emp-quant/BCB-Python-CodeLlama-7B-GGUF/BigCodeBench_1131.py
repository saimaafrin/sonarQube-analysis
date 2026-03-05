
import hashlib
import binascii

def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")

    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()

    updated_count = 0
    for user in users:
        password = user[1]
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (hashed_password, user[0]))
        updated_count += 1

    return updated_count