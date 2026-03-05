import codecs
import os
import glob
DIRECTORY_PATH = './files/'
def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    # List all text files in the specified directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))
    
    # Iterate over each file and convert its encoding
    for file_path in text_files:
        with codecs.open(file_path, 'r', from_encoding) as file:
            content = file.read()
        
        with codecs.open(file_path, 'w', to_encoding) as file:
            file.write(content)