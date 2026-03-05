
import re
import nltk
from sklearn.decomposition import NMF
from sklearn.feature_extraction.text import TfidfVectorizer
# Ensure nltk's stopwords are downloaded
nltk.download('stopwords')
# Constants
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(texts, num_topics):
    """
    Extracts topics from a collection of text documents using Non-Negative Matrix Factorization (NMF).
    
    Parameters:
    texts (list of str): A list of text documents.
    num_topics (int): The number of topics to extract.
    
    Returns:
    list of list of str: A list where each element is a list of words representing a topic.
    """
    # Preprocess the texts
    processed_texts = []
    for text in texts:
        # Remove non-alphanumeric characters (excluding spaces)
        cleaned_text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        cleaned_text = cleaned_text.lower()
        # Remove stopwords
        words = [word for word in cleaned_text.split() if word not in STOPWORDS]
        processed_texts.append(' '.join(words))
    
    # Vectorize the processed texts using TF-IDF
    vectorizer = TfidfVectorizer()
    X = vectorizer.fit_transform(processed_texts)
    
    # Apply NMF to extract the specified number of topics
    nmf = NMF(n_components=num_topics, random_state=42)
    W = nmf.fit_transform(X)
    H = nmf.components_
    
    # Get the most significant words for each topic
    topics = []
    for component in H:
        top_words_indices = component.argsort()[:-11:-1]  # Get the indices of the top 10 words
        top_words = [vectorizer.get_feature_names_out()[i] for i in top_words_indices]
        topics.append(top_words)
    
    return topics