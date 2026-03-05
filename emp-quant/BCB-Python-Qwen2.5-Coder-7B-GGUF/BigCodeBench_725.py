
import codecs
import os
import glob

# Constants
DIRECTORY_PATH = './files/'

def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    # List all text files in the specified directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))
    
    # Iterate over each file
    for file_path in text_files:
        # Open the file with the original encoding
        with codecs.open(file_path, 'r', from_encoding) as file:
            content = file.read()
        
        # Open the file with the new encoding
        with codecs.open(file_path, 'w', to_encoding) as file:
            file.write(content)