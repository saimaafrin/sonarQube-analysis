
import codecs
import os
import zipfile

def task_func(directory_name="latin_files",
              content='Sopetón',
              file_names=['file1.txt', 'file2.txt', 'file3.txt'],
              encoding="latin-1"):
    # Create the directory
    os.makedirs(directory_name, exist_ok=True)
    
    # Create the .txt files and write content to them
    for file_name in file_names:
        with codecs.open(os.path.join(directory_name, file_name), 'w', encoding=encoding) as file:
            file.write(content)
    
    # Zip the directory
    zip_file_name = directory_name + '.zip'
    with zipfile.ZipFile(zip_file_name, 'w') as zipf:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                zipf.write(os.path.join(root, file), os.path.relpath(os.path.join(root, file), directory_name))
    
    # Remove the directory
    os.rmdir(directory_name)
    
    return zip_file_name