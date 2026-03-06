
import re
import nltk
from gensim.models import Word2Vec

# Constants
ALPHANUMERIC = re.compile('[\W_]+')

def task_func(texts, stopwords=None):
    if not stopwords:
        stopwords = set(nltk.corpus.stopwords.words('english'))
    
    # Clean and tokenize the texts
    def clean_text(text):
        text = ALPHANUMERIC.sub(' ', text)
        tokens = text.lower().split()
        return [token for token in tokens if token not in stopwords]
    
    cleaned_texts = [clean_text(text) for text in texts]
    
    # Train Word2Vec model
    word2vec_model = Word2Vec(cleaned_texts, vector_size=100, window=5, min_count=1, workers=4)
    
    return word2vec_model