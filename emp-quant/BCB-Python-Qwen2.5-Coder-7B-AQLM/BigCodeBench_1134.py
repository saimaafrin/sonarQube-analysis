
import os
import glob
import hashlib

def task_func(source_dir, target_dir, prefix='#Hash: '):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory '{source_dir}' does not exist.")
    
    new_files = []
    
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                content = file.read()
                md5_hash = hashlib.md5(content).hexdigest()
                modified_content = prefix + md5_hash + '\n' + content.decode('utf-8')
                
                target_file_path = os.path.join(target_dir, os.path.basename(file_path))
                with open(target_file_path, 'w') as target_file:
                    target_file.write(modified_content)
                
                new_files.append(target_file_path)
    
    return new_files