
import re
import glob
from docx import Document

def task_func(directory_path: str) -> int:
    # Initialize a counter for the number of files processed
    file_count = 0

    # Get a list of all .docx files in the directory
    docx_files = glob.glob(f"{directory_path}/*.docx")

    # Iterate over each .docx file
    for docx_file in docx_files:
        # Open the .docx file
        doc = Document(docx_file)

        # Iterate over each paragraph in the document
        for paragraph in doc.paragraphs:
            # Replace double quotes with \" to escape them
            paragraph.text = re.sub(r'"', r'\"', paragraph.text)

        # Save the modified document
        doc.save(docx_file)

        # Increment the file count
        file_count += 1

    # Return the number of files processed
    return file_count