
import nltk
# Download necessary NLTK data (if not already present)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
from collections import Counter

def task_func(content):
    # Tokenize the content into words
    words = nltk.word_tokenize(content)
    
    # Remove the last word from the list of words
    if len(words) > 0:
        words.pop()
    
    # Tag each word with its corresponding POS tag
    pos_tags = nltk.pos_tag(words)
    
    # Count the occurrences of each POS tag
    pos_counts = Counter(tag for _, tag in pos_tags)
    
    return pos_counts