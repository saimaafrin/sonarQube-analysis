import nltk
from collections import Counter
def task_func(content):
    # Tokenize the sentence into words
    words = nltk.word_tokenize(content)
    # Remove the last word from the list
    words = words[:-1]
    # Tag each word with its Part-of-Speech (POS)
    pos_tags = nltk.pos_tag(words)
    # Extract the POS tags and count their occurrences
    pos_counts = Counter(tag for word, tag in pos_tags)
    return pos_counts