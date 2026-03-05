import hashlib
import binascii
def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")
    
    # SQL query to update passwords
    update_query = """
    UPDATE users
    SET password = ?
    WHERE id = ?
    """
    
    # Counter for the number of users updated
    users_updated = 0
    
    # Assuming the cursor is connected to the SQLite database
    # and the 'users' table has columns 'id' and 'password'
    # Fetch all users
    cursor.execute("SELECT id, password FROM users")
    users = cursor.fetchall()
    
    for user_id, password in users:
        # Hash the password with the provided salt
        hashed_password = hashlib.sha256(salt.encode('utf-8') + password.encode('utf-8')).hexdigest()
        
        # Update the user's password in the database
        cursor.execute(update_query, (hashed_password, user_id))
        users_updated += 1
    
    # Commit the changes to the database
    cursor.connection.commit()
    
    return users_updated