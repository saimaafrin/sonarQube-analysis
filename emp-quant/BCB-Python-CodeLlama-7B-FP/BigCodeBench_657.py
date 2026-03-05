import re
import nltk
from gensim.models import Word2Vec
ALPHANUMERIC = re.compile('[\W_]+')
def task_func(texts, stopwords=None):
    """
    Generate word vectors from a list of texts using the gensim Word2Vec model and nltk.corpus.stopwords.
    The texts are first cleaned by removing all non-alphanumeric characters except space, lowercased, and stop words are removed.
    """
    # Clean the texts
    clean_texts = [re.sub(ALPHANUMERIC, ' ', text.lower()) for text in texts]
    # Remove stop words
    if stopwords is not None:
        clean_texts = [re.sub(stopwords, '', text) for text in clean_texts]
    # Create the Word2Vec model
    model = Word2Vec(clean_texts, size=100, window=5, min_count=5, workers=4)
    return model
texts = ['This is a test text.', 'This is another test text.']
stopwords = nltk.corpus.stopwords.words('english')