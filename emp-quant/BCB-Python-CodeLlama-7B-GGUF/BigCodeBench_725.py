
import codecs
import os
import glob
# Constants
DIRECTORY_PATH = './files/'
def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    # Iterate over all files in the directory
    for file_path in glob.iglob(os.path.join(directory, '**', '*.*'), recursive=True):
        # Check if the file is a text file
        if os.path.isfile(file_path) and file_path.endswith(('.txt', '.csv', '.tsv')):
            # Open the file in the specified encoding
            with codecs.open(file_path, 'r', from_encoding) as f:
                # Read the file contents
                contents = f.read()
            # Close the file
            f.close()
            # Open the file in the desired encoding
            with codecs.open(file_path, 'w', to_encoding) as f:
                # Write the file contents
                f.write(contents)
            # Close the file
            f.close()
    # Return None
    return None