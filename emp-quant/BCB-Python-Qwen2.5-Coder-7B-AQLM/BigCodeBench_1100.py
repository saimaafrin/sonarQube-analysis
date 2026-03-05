
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Remove URLs from the texts
    urls_pattern = re.compile(r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+')
    cleaned_texts = [urls_pattern.sub('', text) for text in texts]
    
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the cleaned texts
    tfidf_matrix = vectorizer.fit_transform(cleaned_texts)
    
    # Get the feature names (words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Convert the TF-IDF matrix to a dense format and round to 8 decimal places
    tfidf_scores = tfidf_matrix.toarray().round(8)
    
    # Create a list of tuples with TF-IDF scores for each document
    tfidf_tuples = [tuple(scores) for scores in tfidf_scores]
    
    return tfidf_tuples, feature_names.tolist()