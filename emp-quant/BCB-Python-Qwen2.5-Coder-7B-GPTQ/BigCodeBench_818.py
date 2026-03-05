import re
import string
PUNCTUATION = string.punctuation
def task_func(text):
    # Remove punctuation using regex and convert to lowercase
    cleaned_text = re.sub(f'[{re.escape(PUNCTUATION)}]', '', text).lower()
    # Split the cleaned text into words
    cleaned_words = cleaned_text.split()
    return cleaned_words