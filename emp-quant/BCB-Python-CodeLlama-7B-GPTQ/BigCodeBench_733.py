import re
import string
def task_func(content):
    """
    Count the non-stop words in a sentence without the last word.
    """
    # Remove punctuation and convert to lowercase
    content = re.sub(r'[^\w\s]', '', content.lower())

    # Split the content into individual words
    words = content.split()

    # Count the number of non-stop words
    count = 0
    for word in words:
        if word not in string.punctuation:
            count += 1

    return count