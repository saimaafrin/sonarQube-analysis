import os
import hashlib
DIRECTORY = "./hashed_files"
def task_func(input_string):
    # Create the directory if it does not exist
    if not os.path.exists(DIRECTORY):
        os.makedirs(DIRECTORY)
    
    # Split the input string into lines and filter out empty lines
    lines = [line.strip() for line in input_string.split('\n') if line.strip()]
    
    # List to store the file paths where hashes are saved
    file_paths = []
    
    # Process each non-empty line
    for line in lines:
        # Hash the line using SHA256
        sha256_hash = hashlib.sha256(line.encode()).hexdigest()
        
        # Create the filename using the first 10 characters of the hash
        filename = sha256_hash[:10] + '.txt'
        
        # Create the full file path
        file_path = os.path.join(DIRECTORY, filename)
        
        # Save the hash to the file
        with open(file_path, 'w') as file:
            file.write(sha256_hash)
        
        # Add the file path to the list
        file_paths.append(file_path)
    
    return file_paths