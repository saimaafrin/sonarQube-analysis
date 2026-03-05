
import re
import glob
from docx import Document

def task_func(directory_path: str) -> int:
    # Initialize counter for number of processed files
    num_processed = 0

    # Loop through all .docx files in the provided directory
    for file in glob.glob(f"{directory_path}/*.docx"):
        # Open the file and create a new document object
        with open(file, "rb") as f:
            doc = Document(f)

        # Search for double quotes in the text and add a backslash before each one
        for paragraph in doc.paragraphs:
            paragraph.text = re.sub(r'"', '\\"', paragraph.text)

        # Save the modified document to the original file
        with open(file, "wb") as f:
            doc.save(f)

        # Increment the number of processed files
        num_processed += 1

    # Return the number of processed files
    return num_processed