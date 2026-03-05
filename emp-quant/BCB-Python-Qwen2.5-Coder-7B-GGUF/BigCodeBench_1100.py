
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
    
    # Get the feature names (unique words)
    feature_names = vectorizer.get_feature_names_out()
    
    # Convert the TF-IDF matrix to a list of tuples
    tfidf_scores = [tuple(tfidf_matrix[i].toarray()[0]) for i in range(tfidf_matrix.shape[0])]
    
    # Round the TF-IDF scores to 8 decimal places
    tfidf_scores = [tuple(round(score, 8) for score in scores) for scores in tfidf_scores]
    
    return tfidf_scores, feature_names.tolist()