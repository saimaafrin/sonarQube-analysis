
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Remove URLs from the text documents
    texts = [re.sub(r'https?://\S+', '', text) for text in texts]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the texts to compute TF-IDF scores
    X = vectorizer.fit_transform(texts)

    # Get the unique words across all documents
    features = vectorizer.get_feature_names()

    # Round the TF-IDF scores to 8 decimal places
    X = np.round(X, 8)

    # Return the TF-IDF scores and the unique words
    return (X.todense(), features)