import re
from sklearn.feature_extraction.text import TfidfVectorizer
def task_func(texts):
    # Remove URLs from the texts
    texts = [re.sub(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', '', text) for text in texts]
    
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the texts to get the TF-IDF scores
    tfidf_matrix = vectorizer.fit_transform(texts)
    
    # Convert the TF-IDF matrix to a dense format and round to 8 decimal places
    tfidf_scores = tfidf_matrix.toarray().round(8)
    
    # Get the list of unique words (features)
    feature_names = vectorizer.get_feature_names_out().tolist()
    
    return (tfidf_scores.tolist(), feature_names)
texts = [
    "https://www.example.com This is a sample text document.",
    "This is another document with different words.",
    "And yet another document with unique words."
]