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
    clean_texts = []
    for text in texts:
        clean_text = re.sub(ALPHANUMERIC, '', text.lower())
        clean_text = ' '.join(clean_text.split())
        clean_text = ' '.join(clean_text.split())
        clean_text = ' '.join(clean_text.split())
        clean_texts.append(clean_text)

    # Remove stop words
    if stopwords is not None:
        stop_words = set(stopwords)
        clean_texts = [text for text in clean_texts if not set(text.split()).intersection(stop_words)]

    # Train the Word2Vec model
    word2vec_model = Word2Vec(clean_texts, size=100, window=5, min_count=5, workers=4)

    return word2vec_model
texts = [
    "This is a sample text.",
    "This is another sample text.",
    "This is a third sample text."
]