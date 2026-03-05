
import re
import glob
from docx import Document

def task_func(directory_path: str) -> int:
    files_processed = 0
    for file_path in glob.glob(f"{directory_path}/*.docx"):
        with Document(file_path) as doc:
            text = doc.text
            new_text = re.sub(r'"', r'\"', text)
            doc.text = new_text
            files_processed += 1
    return files_processed