import re
import nltk
from gensim.models import Word2Vec
ALPHANUMERIC = re.compile('[\W_]+')
def task_func(texts, stopwords=None):
    """
    Generate word vectors from a list of texts using the gensim Word2Vec model and nltk.corpus.stopwords.
    
    Parameters:
    texts (list of str): List of texts to process.
    stopwords (list of str, optional): List of stopwords to remove. If None, uses nltk.corpus.stopwords.words('english').
    
    Returns:
    Word2Vec: A trained Word2Vec model.
    """
    # Download stopwords if not already downloaded
    if stopwords is None:
        nltk.download('stopwords')
        stopwords = nltk.corpus.stopwords.words('english')
    
    # Clean and tokenize the texts
    cleaned_texts = []
    for text in texts:
        # Remove non-alphanumeric characters except space
        cleaned_text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        cleaned_text = cleaned_text.lower()
        # Tokenize
        tokens = cleaned_text.split()
        # Remove stopwords
        tokens = [token for token in tokens if token not in stopwords]
        cleaned_texts.append(tokens)
    
    # Train Word2Vec model
    word2vec_model = Word2Vec(cleaned_texts, vector_size=100, window=5, min_count=1, workers=4)
    
    return word2vec_model