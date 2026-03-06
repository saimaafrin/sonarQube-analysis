
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
    texts (list of str): List of text documents.
    num_topics (int): Number of topics to extract.

    Returns:
    list of list of str: A list where each element is a list of words representing a topic.
    """
    # Preprocess the texts
    def preprocess(text):
        text = ALPHANUMERIC.sub(' ', text)
        text = text.lower()
        words = [word for word in text.split() if word not in STOPWORDS]
        return ' '.join(words)

    processed_texts = [preprocess(text) for text in texts]

    # Vectorize the processed texts using TF-IDF
    vectorizer = TfidfVectorizer(max_df=0.75, min_df=2, stop_words='english')
    X = vectorizer.fit_transform(processed_texts)

    # Apply NMF to extract topics
    nmf = NMF(n_components=num_topics, random_state=42)
    W = nmf.fit_transform(X)
    H = nmf.components_

    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()

    # Extract the top words for each topic
    topics = []
    for topic_idx in range(num_topics):
        top_indices = H[topic_idx].argsort()[:-10 - 1:-1]  # Adjust the slice to get more or fewer words per topic
        topics.append([feature_names[i] for i in top_indices])

    return topics