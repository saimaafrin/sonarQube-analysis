
import re
import nltk
from gensim.models import Word2Vec

# Constants
ALPHANUMERIC = re.compile('[\W_]+')

def task_func(texts, stopwords=None):
    # Clean the texts by removing all non-alphanumeric characters except space
    clean_texts = [re.sub(ALPHANUMERIC, ' ', text) for text in texts]

    # Lowercase the texts
    lowercase_texts = [text.lower() for text in clean_texts]

    # Remove stop words
    stop_words = set(nltk.corpus.stopwords.words('english'))
    filtered_texts = [text for text in lowercase_texts if text not in stop_words]

    # Create a Word2Vec model
    model = Word2Vec(filtered_texts, size=100, window=5, min_count=5, workers=4)

    return model

# Print the word vectors
print(model.wv['this'])
print(model.wv['sample'])