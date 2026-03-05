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
    # Remove the last word
    words = words[:-1]
    # Count the number of non-stop words
    count = len([word for word in words if word.isalpha()])
    return count