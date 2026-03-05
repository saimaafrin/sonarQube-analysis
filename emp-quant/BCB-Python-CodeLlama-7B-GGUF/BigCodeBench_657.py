
import re
import nltk
from gensim.models import Word2Vec
# Constants
ALPHANUMERIC = re.compile('[\W_]+')
def task_func(texts, stopwords=None):
    # Clean the texts by removing all non-alphanumeric characters except space
    clean_texts = [re.sub(ALPHANUMERIC, ' ', text.lower()) for text in texts]
    # Remove stop words
    if stopwords is not None:
        stop_words = set(stopwords)
        clean_texts = [[word for word in text.split() if word not in stop_words] for text in clean_texts]
    # Create a Word2Vec model
    model = Word2Vec(clean_texts, size=100, window=5, min_count=1, workers=4)
    return model