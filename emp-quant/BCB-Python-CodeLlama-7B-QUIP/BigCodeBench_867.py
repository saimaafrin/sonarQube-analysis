
import re
import string

def task_func(text1, text2):
    # Remove any ASCII punctuation from the texts
    cleaned_text1 = re.sub(r'[' + string.punctuation + ']', '', text1)
    cleaned_text2 = re.sub(r'[' + string.punctuation + ']', '', text2)
    return (cleaned_text1, cleaned_text2)