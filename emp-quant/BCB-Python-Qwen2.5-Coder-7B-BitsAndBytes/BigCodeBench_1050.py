
import os
import hashlib

# Constants
DIRECTORY = "./hashed_files"

def task_func(input_string):
    # Ensure the directory exists
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    # Split the input string into lines and filter out empty ones
    lines = [line.strip() for line in input_string.split('\n') if line.strip()]
    
    # List to store the file paths where hashes are saved
    file_paths = []
    
    # Process each line
    for line in lines:
        # Hash the line using SHA256
        sha256_hash = hashlib.sha256(line.encode()).hexdigest()
        
        # Create the filename based on the first 10 characters of the hash
        filename = sha256_hash[:10] + ".txt"
        filepath = os.path.join(DIRECTORY, filename)
        
        # Save the hash to the file
        with open(filepath, 'w') as file:
            file.write(sha256_hash)
        
        # Add the file path to the list
        file_paths.append(filepath)
    
    return file_paths