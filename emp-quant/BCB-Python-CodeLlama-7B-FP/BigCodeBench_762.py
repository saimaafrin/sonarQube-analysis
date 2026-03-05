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
    zipped_file = zipfile.ZipFile(directory_name + '.zip', 'w')
    for file_name in file_names:
        zipped_file.write(os.path.join(directory_name, file_name), file_name)
    zipped_file.close()

    # Return the zipped file name
    return directory_name + '.zip'
directory_name = "latin_files"
content = 'Sopetón'
file_names = ['file1.txt', 'file2.txt', 'file3.txt']
encoding = "latin-1"