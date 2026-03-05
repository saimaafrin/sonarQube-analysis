
import codecs
import os
import zipfile

def task_func(directory_name="latin_files",
          content='Sopetón',
          file_names=['file1.txt', 'file2.txt', 'file3.txt'],
          encoding="latin-1"):
    # Create the directory
    if not os.path.exists(directory_name):
        os.makedirs(directory_name)

    # Create the files
    for file_name in file_names:
        with open(os.path.join(directory_name, file_name), 'w', encoding=encoding) as f:
            f.write(content)

    # Zip the directory
    zip_file_name = directory_name + '.zip'
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zf:
        for root, dirs, files in os.walk(directory_name):
            for file in files:
                file_path = os.path.join(root, file)
                zf.write(file_path, file_path)

    return zip_file_name