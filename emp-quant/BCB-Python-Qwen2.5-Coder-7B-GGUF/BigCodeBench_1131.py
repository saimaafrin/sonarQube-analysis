
import hashlib
import binascii

def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")
    
    # SQL query to update passwords
    update_query = "UPDATE users SET password = ? WHERE id = ?"
    
    # Counter for the number of users updated
    updated_count = 0
    
    # Assuming the user table has columns 'id' and 'password'
    # Fetch all users from the table
    cursor.execute("SELECT id, password FROM users")
    users = cursor.fetchall()
    
    for user in users:
        user_id, password = user
        # Hash the password with the provided salt
        hashed_password = hashlib.sha256(salt.encode() + password.encode()).hexdigest()
        # Update the user's password in the database
        cursor.execute(update_query, (hashed_password, user_id))
        updated_count += 1
    
    # Commit the changes to the database
    cursor.connection.commit()
    
    return updated_count