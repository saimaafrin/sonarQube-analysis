
import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory '{source_dir}' does not exist")

    # Create the target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Get a list of all files in the source directory
    file_paths = glob.glob(os.path.join(source_dir, '*'))

    # Iterate over the files and compute the MD5 hash
    for file_path in file_paths:
        with open(file_path, 'rb') as file:
            file_content = file.read()
            file_hash = hashlib.md5(file_content).hexdigest()
            file_name = os.path.basename(file_path)
            new_file_path = os.path.join(target_dir, f'{file_hash}_{file_name}')
            with open(new_file_path, 'wb') as new_file:
                new_file.write(f'{prefix}{file_hash}\n'.encode('utf-8'))
                new_file.write(file_content)

    # Return a list of the newly created files
    return [os.path.join(target_dir, f) for f in os.listdir(target_dir)]