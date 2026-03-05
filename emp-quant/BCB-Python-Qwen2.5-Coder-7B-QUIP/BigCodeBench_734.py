
import nltk
# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter

def task_func(content):
    # Tokenize the content into words
    words = nltk.word_tokenize(content)
    # Remove the last word from the list
    words = words[:-1]
    # Tag each word with its Part-of-Speech
    pos_tags = nltk.pos_tag(words)
    # Extract the POS tags and count their occurrences
    pos_counts = Counter(tag for _, tag in pos_tags)
    return dict(pos_counts)