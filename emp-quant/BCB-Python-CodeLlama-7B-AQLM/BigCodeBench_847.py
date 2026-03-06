import re
import os
import string
import random
def task_func(input_string, directory='./text_files'):
    """
    Split a multi-line string into separate strings, remove special characters, and save each string as a separate text file.
    
    Parameters:
    - input_string (str): The multi-line string to be split and saved.
    - directory (str): The directory where the text files will be saved. Default is './text_files'.
    
    Returns:
    - file_paths (list): A list of file paths where the text is saved.
    
    Requirements:
    - re
    - os
    - string
    - random 
    
    Example:
    >>> task_func('line a\nfollows by line b\n...bye\n')
    ['./text_files/12345.txt', './text_files/67890.txt', './text_files/11223.txt']
    """
    # split the string into separate lines
    lines = input_string.split('\n')
    
    # remove special characters
    lines = [re.sub('[^a-zA-Z0-9\s]', '', line) for line in lines]
    
    # create a random file name
    file_name = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5))
    
    # create a file path
    file_path = os.path.join(directory, file_name + '.txt')
    
    # save the string as a text file
    with open(file_path, 'w') as f:
        f.write('\n'.join(lines))
    
    # return the file path
    return file_path