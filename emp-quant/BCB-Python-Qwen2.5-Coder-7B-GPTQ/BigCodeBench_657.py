import re
import nltk
from gensim.models import Word2Vec
from nltk.corpus import stopwords
ALPHANUMERIC = re.compile('[\W_]+')
def task_func(texts, stopwords=None):
    if stopwords is None:
        stopwords = set(nltk.corpus.stopwords.words('english'))
    
    # Clean and preprocess the texts
    cleaned_texts = []
    for text in texts:
        # Remove non-alphanumeric characters except space
        cleaned_text = ALPHANUMERIC.sub(' ', text)
        # Lowercase
        cleaned_text = cleaned_text.lower()
        # Tokenize
        tokens = nltk.word_tokenize(cleaned_text)
        # Remove stop words
        tokens = [word for word in tokens if word not in stopwords]
        cleaned_texts.append(tokens)
    
    # Train Word2Vec model
    word2vec_model = Word2Vec(cleaned_texts, vector_size=100, window=5, min_count=1, workers=4)
    
    return word2vec_model