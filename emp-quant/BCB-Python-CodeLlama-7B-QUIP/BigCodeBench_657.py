
import re
import nltk
from gensim.models import Word2Vec
# Constants
ALPHANUMERIC = re.compile('[\W_]+')
def task_func(texts, stopwords=None):
    # Clean the texts
    cleaned_texts = [re.sub(ALPHANUMERIC, ' ', text).lower() for text in texts]
    # Remove stopwords
    if stopwords:
        stop_words = nltk.corpus.stopwords.words('english')
        cleaned_texts = [word for word in cleaned_texts if word not in stop_words]
    # Create the Word2Vec model
    model = Word2Vec(cleaned_texts, size=100, window=5, min_count=1, seed=1)
    return model