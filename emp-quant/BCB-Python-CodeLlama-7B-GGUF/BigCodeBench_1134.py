
import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f'Source directory {source_dir} does not exist')

    # Create target directory if it does not exist
    if not os.path.exists(target_dir):
        os.makedirs(target_dir)

    # Get list of files in source directory
    files = glob.glob(os.path.join(source_dir, '*'))

    # Iterate over files and compute MD5 hash
    for file in files:
        with open(file, 'rb') as f:
            content = f.read()
            hash = hashlib.md5(content).hexdigest()
            new_file = os.path.join(target_dir, f'{hash}.txt')
            with open(new_file, 'wb') as f:
                f.write(prefix.encode('utf-8'))
                f.write(content)

    # Return list of new files
    return [os.path.relpath(new_file, target_dir) for new_file in glob.glob(os.path.join(target_dir, '*'))]