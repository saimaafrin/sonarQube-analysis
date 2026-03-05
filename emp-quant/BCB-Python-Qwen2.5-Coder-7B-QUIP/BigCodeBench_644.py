
import hashlib
import base64

def task_func(filename, data, password):
    # Generate a hash from the password
    password_hash = hashlib.sha256(password.encode()).hexdigest()
    
    # Encrypt the data using the hash
    encrypted_data = base64.b64encode(data.encode()).decode() + password_hash
    
    # Write the encrypted data to a file
    try:
        with open(filename, 'w') as file:
            file.write(encrypted_data)
    except FileNotFoundError:
        # Create the directory if it does not exist
        directory = filename.split('/')[0]
        if not os.path.exists(directory):
            os.makedirs(directory)
        with open(filename, 'w') as file:
            file.write(encrypted_data)
    
    # Return the encrypted string
    return encrypted_data