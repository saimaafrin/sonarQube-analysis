
import re
import glob
from docx import Document

def task_func(directory_path: str) -> int:
    # Initialize counter for number of .docx files processed
    num_files_processed = 0

    # Loop through all .docx files in the directory
    for file in glob.glob(directory_path + "/*.docx"):
        # Open the .docx file
        doc = Document(file)

        # Search for double quotes in the text
        for paragraph in doc.paragraphs:
            text = paragraph.text
            new_text = re.sub(r'"', '\\"', text)
            paragraph.text = new_text

        # Save the modified .docx file
        doc.save(file)

        # Increment the counter
        num_files_processed += 1

    # Return the number of .docx files processed
    return num_files_processed