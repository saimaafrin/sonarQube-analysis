
import re
import glob
from docx import Document

def task_func(directory_path: str) -> int:
    # Initialize the count of processed files
    processed_files = 0
    
    # Use glob to find all .docx files in the specified directory
    docx_files = glob.glob(f"{directory_path}/*.docx")
    
    # Iterate over each file found
    for file_path in docx_files:
        # Load the document
        doc = Document(file_path)
        
        # Iterate over all paragraphs in the document
        for paragraph in doc.paragraphs:
            # Replace double quotes with escaped double quotes
            paragraph.text = re.sub(r'"', r'\"', paragraph.text)
        
        # Save the modified document
        doc.save(file_path)
        
        # Increment the count of processed files
        processed_files += 1
    
    # Return the number of files processed
    return processed_files