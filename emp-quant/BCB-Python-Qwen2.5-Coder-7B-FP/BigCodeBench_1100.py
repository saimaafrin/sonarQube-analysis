import re
from sklearn.feature_extraction.text import TfidfVectorizer
def task_func(texts):
    # Remove URLs from the texts
    texts = [re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text) for text in texts]
    
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the texts to get the TF-IDF matrix
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Get the feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Convert the TF-IDF matrix to a list of tuples
    tfidf_tuples = [tuple(tfidf_matrix[i].toarray()[0]) for i in range(tfidf_matrix.shape[0])]
    
    # Round the TF-IDF scores to 8 decimal places
    tfidf_tuples = [tuple(round(score, 8) for score in doc) for doc in tfidf_tuples]
    
    return tfidf_tuples, feature_names.tolist()