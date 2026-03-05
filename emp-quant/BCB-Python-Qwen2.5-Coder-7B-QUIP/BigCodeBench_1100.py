
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Remove URLs from the texts
    urls = re.compile(r'http[s]?://\S+|www\.\S+')
    texts = [re.sub(urls, '', text) for text in texts]

    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(texts)

    # Get the feature names (words) and the TF-IDF scores
    feature_names = vectorizer.get_feature_names_out()
    tfidf_scores = tfidf_matrix.toarray()

    # Round the TF-IDF scores to 8 decimal places
    tfidf_scores = tfidf_scores.round(8)

    # Return the results as specified
    return (list(zip(*tfidf_scores)), list(feature_names))