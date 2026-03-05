import re
import string
PUNCTUATION = string.punctuation
def task_func(text):
    # Remove punctuation using regex
    cleaned_text = re.sub(f'[{re.escape(PUNCTUATION)}]', '', text)
    # Convert to lowercase
    cleaned_text = cleaned_text.lower()
    # Split into words
    cleaned_words = cleaned_text.split()
    return cleaned_words