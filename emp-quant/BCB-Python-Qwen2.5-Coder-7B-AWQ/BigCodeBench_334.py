from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
def task_func(documents):
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
    
    # Fit and transform the documents to get the TF-IDF scores
    tfidf_scores = vectorizer.fit_transform(documents)
    
    # Convert the TF-IDF scores to a pandas DataFrame
    tfidf_df = pd.DataFrame(tfidf_scores.toarray(), columns=vectorizer.get_feature_names_out())
    
    return tfidf_df