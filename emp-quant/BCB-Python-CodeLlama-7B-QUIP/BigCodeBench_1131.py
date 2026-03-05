
import hashlib
import binascii

def task_func(salt, cursor):
    if type(salt) != str:
        raise TypeError("Salt must be a string")
    users = cursor.execute("SELECT * FROM users")
    for user in users:
        user_id = user[0]
        user_name = user[1]
        user_password = user[2]
        salted_password = hashlib.sha256(user_password.encode()).hexdigest()
        cursor.execute("UPDATE users SET password = ? WHERE id = ?", (salted_password, user_id))
    return len(users)