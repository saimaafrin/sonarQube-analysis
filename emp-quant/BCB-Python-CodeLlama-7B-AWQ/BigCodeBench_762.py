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
    zipped_file = zipfile.ZipFile(os.path.join(directory_name, 'directorio.zip'), 'w')
    zipped_file.write(directory_name)
    zipped_file.close()

    # Clean up
    shutil.rmtree(directory_name)

    return os.path.join(directory_name, 'directorio.zip')
directory_name = "directorio"
content = "Sopetón"
file_names = ["custom1.txt", "custom2.txt", "custom3.txt"]
encoding = "utf-8"