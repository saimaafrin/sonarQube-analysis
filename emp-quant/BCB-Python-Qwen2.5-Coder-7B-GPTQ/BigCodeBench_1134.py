import os
import glob
import hashlib
def task_func(source_dir, target_dir, prefix='#Hash: '):
    if not os.path.exists(source_dir):
        raise FileNotFoundError(f"The source directory {source_dir} does not exist.")
    
    new_files = []
    for file_path in glob.glob(os.path.join(source_dir, '*')):
        if os.path.isfile(file_path):
            with open(file_path, 'rb') as file:
                file_content = file.read()
                md5_hash = hashlib.md5(file_content).hexdigest()
                new_content = prefix + md5_hash + '\n' + file_content.decode('utf-8')
                
                relative_path = os.path.relpath(file_path, source_dir)
                new_file_path = os.path.join(target_dir, relative_path)
                os.makedirs(os.path.dirname(new_file_path), exist_ok=True)
                
                with open(new_file_path, 'w') as new_file:
                    new_file.write(new_content)
                
                new_files.append(new_file_path)
    
    return new_files