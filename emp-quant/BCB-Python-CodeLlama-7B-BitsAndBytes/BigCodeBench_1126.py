
import re
import hashlib

def task_func(input_str):
    # Remove special characters, punctuation marks, and spaces from the input string
    cleaned_str = re.sub(r'[^a-zA-Z0-9]', '', input_str)

    # Hash the cleaned string with SHA256
    hashed_str = hashlib.sha256(cleaned_str.encode()).hexdigest()

    return hashed_str