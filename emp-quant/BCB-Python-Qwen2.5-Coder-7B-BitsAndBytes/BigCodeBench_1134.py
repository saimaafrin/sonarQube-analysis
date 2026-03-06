
import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
    
    # Create the target directory if it doesn't exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)
    
    # List to store the paths of the newly created files
    new_files = []
    
    # Iterate over all files in the source directory
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        if os.path.isfile(file_path):
            # Read the content of the file
            with open(file_path, 'rb') as file:
                content = file.read()
            
            # Compute the MD5 hash of the file content
            md5_hash = hashlib.md5(content).hexdigest()
            
            # Prepend the hash and prefix to the original content
            new_content = (prefix + md5_hash + '\n' + content.decode('utf-8')).encode('utf-8')
            
            # Generate the path for the new file in the target directory
            base_name = os.path.basename(file_path)
            new_file_path = os.path.join(target_dir, base_name)
            
            # Write the modified content to the new file
            with open(new_file_path, 'wb') as new_file:
                new_file.write(new_content)
            
            # Add the path of the new file to the list
            new_files.append(new_file_path)
    
    return new_files