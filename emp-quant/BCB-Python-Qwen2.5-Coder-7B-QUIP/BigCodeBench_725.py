
import codecs
import os
import glob
# Constants
DIRECTORY_PATH = './files/'
def task_func(directory=DIRECTORY_PATH, from_encoding='cp1251', to_encoding='utf8'):
    """
    Converts the encoding of all text files in a specified directory from one encoding to another.
    The function modifies the files in-place.
    """
    # Ensure the directory exists
    if not os.path.exists(directory):
        print(f"Directory {directory} does not exist.")
        return

    # Get a list of all text files in the directory
    text_files = glob.glob(os.path.join(directory, '*.txt'))

    # Iterate over the text files and convert their encoding
    for file_path in text_files:
        try:
            # Open the file with the original encoding
            with codecs.open(file_path, 'r', encoding=from_encoding) as file:
                content = file.read()

            # Write the content with the new encoding
            with codecs.open(file_path, 'w', encoding=to_encoding) as file:
                file.write(content)

            print(f"Converted {file_path} from {from_encoding} to {to_encoding}")
        except Exception as e:
            print(f"Error converting {file_path}: {e}")

    print("All files have been converted.")