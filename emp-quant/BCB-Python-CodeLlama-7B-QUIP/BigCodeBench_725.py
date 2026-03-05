
import codecs
import os
import glob

# Constants
DIRECTORY_PATH = './files/'

def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    for file_path in glob.glob(f'{directory}/*'):
        with codecs.open(file_path, 'r', from_encoding) as f:
            content = f.read()
        with codecs.open(file_path, 'w', to_encoding) as f:
            f.write(content)

task_func()