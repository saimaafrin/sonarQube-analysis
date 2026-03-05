
import re
import string

def task_func(content):
    # Remove punctuation and convert to lowercase
    content = re.sub(r'[^\w\s]', '', content.lower())

    # Split the content into words
    words = content.split()

    # Remove the last word
    words = words[:-1]

    # Count the number of non-stop words
    count = len(words)

    return count