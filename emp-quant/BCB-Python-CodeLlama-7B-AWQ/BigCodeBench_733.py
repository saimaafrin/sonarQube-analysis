import re
import string
def task_func(content):
    """
    Count the non-stop words in a sentence without the last word.
    """
    # Remove punctuation and convert to lowercase
    content = re.sub(r'[^\w\s]', '', content.lower())
    # Split the content into words
    words = content.split()
    # Remove the last word
    words = words[:-1]
    # Count the number of words
    count = len(words)
    return count