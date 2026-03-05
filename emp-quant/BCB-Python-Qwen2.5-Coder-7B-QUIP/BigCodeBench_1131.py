
import hashlib
import binascii

def task_func(salt, cursor):
    if not isinstance(salt, str):
        raise TypeError("Salt must be a string")
    
    # Prepare the SQL query to update the passwords
    sql = "UPDATE user SET password = ? WHERE id = ?"
    
    # Initialize a counter for the number of users updated
    updated_count = 0
    
    # Iterate over all users and update their passwords
    for user_id in cursor.connection.execute("SELECT id FROM user"):
        # Hash the password using the provided salt
        hashed_password = hashlib.sha256(salt.encode() + user_id[0].encode()).hexdigest()
        
        # Update the user's password in the database
        cursor.execute(sql, (hashed_password, user_id[0]))
        
        # Increment the counter
        updated_count += 1
    
    # Return the number of users whose passwords were updated
    return updated_count