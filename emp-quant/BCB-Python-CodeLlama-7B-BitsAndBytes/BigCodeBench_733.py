
import re
import string

def task_func(content):
    # Remove punctuation and convert to lowercase
    content = re.sub(r'[^\w\s]', '', content.lower())

    # Split the content into words
    words = content.split()

    # Count the number of words that are not stopwords
    count = 0
    for word in words:
        if word not in string.stopwords:
            count += 1

    return count