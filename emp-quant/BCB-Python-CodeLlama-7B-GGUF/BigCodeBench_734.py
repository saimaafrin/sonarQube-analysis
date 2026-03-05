
import nltk
# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter

def count_pos_tags(sentence):
    """
    Count the part-of-speech (POS) tags in a sentence without the last word.

    Args:
        sentence (str): The sentence to count POS tags for.

    Returns:
        dict: A dictionary with POS tags as keys and their count as values.
    """
    # Tokenize the sentence
    tokens = nltk.word_tokenize(sentence)

    # Remove the last word (the last token)
    tokens = tokens[:-1]

    # Tag the remaining tokens
    tagged_tokens = nltk.pos_tag(tokens)

    # Count the POS tags
    pos_tag_counts = Counter([tag for word, tag in tagged_tokens])

    return pos_tag_counts