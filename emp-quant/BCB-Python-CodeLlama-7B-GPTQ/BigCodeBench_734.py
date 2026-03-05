import nltk
from collections import Counter
def task_func(content):
    # Tokenize the input text
    tokens = nltk.word_tokenize(content)
    # Remove the last word from the token list
    tokens = tokens[:-1]
    # Use the POS tagger to assign POS tags to the remaining tokens
    tagged_tokens = nltk.pos_tag(tokens)
    # Create a dictionary with POS tags as keys and their count as values
    pos_counts = Counter(tag for tag, _ in tagged_tokens)
    return pos_counts
content = "The quick brown fox jumps over the lazy dog."