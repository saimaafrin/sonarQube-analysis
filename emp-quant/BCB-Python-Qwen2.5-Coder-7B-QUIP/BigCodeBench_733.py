
import re
import string
def task_func(content):
    # Remove punctuation and convert to lowercase
    content = re.sub(f"[{re.escape(string.punctuation)}]", "", content).lower()
    # Split the content into words
    words = content.split()
    # Remove the last word
    words = words[:-1]
    # Count the non-stop words
    count = len(words)
    return count