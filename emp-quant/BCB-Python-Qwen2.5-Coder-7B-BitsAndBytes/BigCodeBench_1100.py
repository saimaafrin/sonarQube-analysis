
import re
from sklearn.feature_extraction.text import TfidfVectorizer

def task_func(texts):
    # Remove URLs from the texts
    urls_pattern = r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\\(\\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    cleaned_texts = [re.sub(urls_pattern, '', text) for text in texts]
    
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit and transform the cleaned texts
    tfidf_matrix = vectorizer.fit_transform(cleaned_texts)
    
    # Get the feature names
    feature_names = vectorizer.get_feature_names_out().tolist()
    
    # Convert the TF-IDF matrix to a list of tuples
    tfidf_scores = [tuple(tfidf_matrix[i].toarray()[0]) for i in range(len(tfidf_matrix))]
    
    return (tfidf_scores, feature_names)

result = task_func(texts)
print(result)