
import re
import string

def task_func(content):
    # Remove the last word in the sentence
    sentence = re.sub(r'\s+[a-zA-Z]+\s*$', '', content)

    # Count the number of words in the remaining sentence
    count = len(re.split(r'\s+', sentence))

    return count