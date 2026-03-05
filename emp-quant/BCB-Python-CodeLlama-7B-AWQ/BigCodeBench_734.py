import nltk
from collections import Counter
def task_func(content):
    # Tokenize the input text
    tokens = nltk.word_tokenize(content)
    # Remove the last word
    tokens = tokens[:-1]
    # Tag the remaining words
    tags = nltk.pos_tag(tokens)
    # Count the tags
    tag_counts = Counter(tags)
    # Return the dictionary of tag counts
    return tag_counts
content = "This is a sample sentence."