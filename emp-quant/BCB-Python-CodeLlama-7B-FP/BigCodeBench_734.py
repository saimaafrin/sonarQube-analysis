import nltk
from collections import Counter
def task_func(content):
    """
    Count the POS tags in a sentence without the last word.
    :param content: The sentence to be processed.
    :return: A dictionary with POS tags as keys and their count as values.
    """
    # Tokenize the sentence
    tokens = nltk.word_tokenize(content)
    # Remove the last word
    tokens = tokens[:-1]
    # Tag the remaining words
    tags = nltk.pos_tag(tokens)
    # Count the tags
    tag_counts = Counter(tag for word, tag in tags)
    return tag_counts
content = "The quick brown fox jumps over the lazy dog."