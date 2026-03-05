
import codecs
import os
import glob

# Constants
DIRECTORY_PATH = './files/'

def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    # List all text files in the specified directory
    files = glob.glob(os.path.join(directory, '*.txt'))
    
    # Iterate over each file
    for file_path in files:
        # Open the file with the original encoding
        with codecs.open(file_path, 'r', encoding=from_encoding) as file:
            content = file.read()
        
        # Open the file with the new encoding
        with codecs.open(file_path, 'w', encoding=to_encoding) as file:
            file.write(content)
    
    # Return None as per the requirement
    return None