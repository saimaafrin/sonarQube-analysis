
import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory {source_dir} does not exist.")

    # Create a list of files in the source directory
    file_paths = glob.glob(os.path.join(source_dir, '*'))

    # Initialize the list of files to be created in the target directory
    created_files = []

    # Iterate over the files in the source directory
    for file_path in file_paths:
        # Get the file name and the file content
        file_name = os.path.basename(file_path)
        file_content = open(file_path, 'rb').read()

        # Compute the MD5 hash of the file content
        hash_value = hashlib.md5(file_content).hexdigest()

        # Prepend the hash to the file content
        modified_content = prefix + hash_value + file_content

        # Write the modified content to a new file in the target directory
        target_file_path = os.path.join(target_dir, file_name)
        with open(target_file_path, 'wb') as f:
            f.write(modified_content)

        # Add the target file path to the list of created files
        created_files.append(target_file_path)

    return created_files