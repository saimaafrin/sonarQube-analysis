
import re
import string

def task_func(text1, text2):
    # Remove ASCII punctuation from the input strings
    cleaned_text1 = re.sub(r'[^\w\s]', '', text1)
    cleaned_text2 = re.sub(r'[^\w\s]', '', text2)

    # Return the cleaned strings as a tuple
    return (cleaned_text1, cleaned_text2)