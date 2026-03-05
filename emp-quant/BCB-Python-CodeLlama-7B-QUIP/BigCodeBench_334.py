
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def task_func(documents):
    # Tokenize the words in each document
    documents_tokenized = [word_tokenize(doc) for doc in documents]
    
    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer to the tokenized documents
    vectorizer.fit(documents_tokenized)
    
    # Get the TF-IDF scores for each word in each document
    scores = vectorizer.transform(documents_tokenized)
    
    # Create a DataFrame with the scores
    scores_df = pd.DataFrame(scores, columns=vectorizer.get_feature_names())
    
    return scores_df