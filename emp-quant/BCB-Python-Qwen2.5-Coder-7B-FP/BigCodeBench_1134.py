import os
import glob
import hashlib
def task_func(source_dir, target_dir, prefix='#Hash: '):
    # Check if the source directory exists
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
    
    # List to store paths of newly created files
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
            modified_content = prefix + md5_hash + '\n' + content.decode('utf-8')
            
            # Construct the path for the new file in the target directory
            new_file_path = os.path.join(target_dir, os.path.basename(file_path))
            
            # Write the modified content to the new file
            with open(new_file_path, 'w') as new_file:
                new_file.write(modified_content)
            
            # Append the path of the new file to the list
            new_files.append(new_file_path)
    
    return new_files