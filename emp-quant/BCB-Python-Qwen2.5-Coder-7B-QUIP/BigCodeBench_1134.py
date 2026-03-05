
import os
import glob
import hashlib
def task_func(source_dir, target_dir, prefix='#Hash: '):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"Source directory {source_dir} does not exist.")
    
    created_files = []
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        if os.path.isfile(file_path):
            with open(file_path, 'r') as file:
                content = file.read()
                file_hash = hashlib.md5(content.encode()).hexdigest()
                new_file_path = os.path.join(target_dir, os.path.basename(file_path))
                with open(new_file_path, 'w') as new_file:
                    new_file.write(f"{prefix}{file_hash}\n{content}")
                created_files.append(new_file_path)
    
    return created_files