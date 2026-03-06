
import hashlib
import binascii

def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")
    
    # SQL query to update passwords
    update_query = "UPDATE users SET password = ? WHERE id = ?"
    
    # Counter for successful updates
    success_count = 0
    
    # Assuming 'users' table has columns 'id', 'password'
    cursor.execute("SELECT id, password FROM users")
    rows = cursor.fetchall()
    
    for row in rows:
        user_id, old_password = row
        
        # Hashing the old password with the provided salt
        hashed_password = hashlib.sha256((old_password + salt).encode()).hexdigest()
        
        # Updating the password in the database
        cursor.execute(update_query, (hashed_password, user_id))
        success_count += 1
    
    return success_count