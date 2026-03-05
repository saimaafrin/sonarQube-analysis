
import codecs
import os
import zipfile

def task_func(directory_name="latin_files",
          content='Sopetón',
          file_names=['file1.txt', 'file2.txt', 'file3.txt'],
          encoding="latin-1"):
    # Create the directory
    os.makedirs(directory_name)

    # Create the files
    for file_name in file_names:
        with codecs.open(os.path.join(directory_name, file_name), 'w', encoding=encoding) as f:
            f.write(content)

    # Zip the directory
    zipped_file = directory_name + '.zip'
    with zipfile.ZipFile(zipped_file, 'w', zipfile.ZIP_DEFLATED) as zf:
        for file_name in file_names:
            zf.write(os.path.join(directory_name, file_name))

    return zipped_file