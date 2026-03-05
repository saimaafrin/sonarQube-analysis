
import nltk
# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter

def task_func(content):
    # Tokenize the sentence
    tokens = nltk.word_tokenize(content)
    # Part-of-Speech tag the sentence
    pos_tags = nltk.pos_tag(tokens)
    # Remove the last word
    pos_tags = pos_tags[:-1]
    # Count the POS tags
    pos_counts = Counter(pos_tags)
    return pos_counts