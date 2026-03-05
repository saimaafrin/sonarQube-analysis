
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def task_func(documents):
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer(tokenizer=word_tokenize, stop_words='english')
    
    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Convert the result to a DataFrame
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    
    return tfidf_df