
import re
import string

def task_func(text1, text2):
    # Remove ASCII punctuation from text1 and text2
    cleaned_text1 = re.sub(r'[^\w\s]', '', text1)
    cleaned_text2 = re.sub(r'[^\w\s]', '', text2)

    # Return the cleaned texts as a tuple
    return (cleaned_text1, cleaned_text2)

cleaned_text1, cleaned_text2 = task_func(text1, text2)

print(cleaned_text1, cleaned_text2)