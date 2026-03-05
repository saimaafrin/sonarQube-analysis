import hashlib
import binascii
def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")
    
    # SQL query to update passwords
    update_query = "UPDATE users SET password = ? WHERE id = ?"
    
    # Counter for successful updates
    successful_updates = 0
    
    # Fetch all users from the database
    cursor.execute("SELECT id, password FROM users")
    users = cursor.fetchall()
    
    for user in users:
        user_id, user_password = user
        
        # Hash the password with the provided salt
        hashed_password = hashlib.sha256(salt.encode() + user_password.encode()).hexdigest()
        
        # Update the user's password in the database
        cursor.execute(update_query, (hashed_password, user_id))
        
        # Increment the counter for successful updates
        successful_updates += 1
    
    # Commit the changes to the database
    cursor.connection.commit()
    
    return successful_updates