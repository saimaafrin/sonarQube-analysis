
import codecs
import os
import zipfile

def task_func(directory_name="latin_files",
              content='Sopetón',
              file_names=['file1.txt', 'file2.txt', 'file3.txt'],
              encoding="latin-1"):
    # Create the directory
    os.makedirs(directory_name, exist_ok=True)
    
    # Create and write to the .txt files
    for file_name in file_names:
        file_path = os.path.join(directory_name, file_name)
        with codecs.open(file_path, 'w', encoding=encoding) as file:
            file.write(content)
    
    # Zip the directory
    zip_path = directory_name + '.zip'
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=directory_name)
                zipf.write(file_path, arcname)
    
    # Remove the directory
    os.rmdir(directory_name)
    
    return zip_path