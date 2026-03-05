import re
import glob
from docx import Document
def task_func(directory_path: str) -> int:
    """
    Processes all Word (.docx) files in the provided directory, searching for double quotes in the text and adding a backslash before each double quote to "protect" it.
    The function should output with:
        int: Number of .docx files processed.
    """
    # Initialize variables
    docx_files = glob.glob(directory_path + '/*.docx')
    num_processed = 0

    # Iterate over all .docx files in the directory
    for file in docx_files:
        # Open the .docx file
        with Document(file) as doc:
            # Search for double quotes in the text
            text = doc.text
            matches = re.findall(r'"', text)

            # Add a backslash before each double quote
            for match in matches:
                text = text.replace(match, '\\' + match)

            # Save the modified text to the .docx file
            doc.text = text

        # Increment the number of .docx files processed
        num_processed += 1

    # Return the number of .docx files processed
    return num_processed
directory_path = 'path/to/directory'