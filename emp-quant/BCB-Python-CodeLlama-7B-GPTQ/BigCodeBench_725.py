import codecs
import os
import glob
DIRECTORY_PATH = './files/'
def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    """
    Convert the encoding of all text files in a specified directory from one encoding to another.
    The function modifies the files in-place.
    """
    for file in glob.glob(os.path.join(directory, '*.txt')):
        with codecs.open(file, 'r', from_encoding) as f:
            content = f.read()
        with codecs.open(file, 'w', to_encoding) as f:
            f.write(content)
    return None