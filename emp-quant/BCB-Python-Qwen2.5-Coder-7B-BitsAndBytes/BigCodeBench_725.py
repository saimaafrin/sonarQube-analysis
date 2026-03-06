
import codecs
import os
import glob

# Constants
DIRECTORY_PATH = './files/'

def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    # List all text files in the specified directory
    file_paths = glob.glob(os.path.join(directory, '*.txt'))
    
    for file_path in file_paths:
        try:
            # Read the content of the file with the original encoding
            with codecs.open(file_path, 'r', from_encoding) as file:
                content = file.read()
            
            # Write the content back to the file with the new encoding
            with codecs.open(file_path, 'w', to_encoding) as file:
                file.write(content)
        
        except Exception as e:
            print(f"Error processing {file_path}: {e}")