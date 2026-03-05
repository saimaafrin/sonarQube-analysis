from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
def task_func(documents):
    """
    Calculate the TF-IDF score of the words in a list of documents.
    
    Parameters:
    documents (list of str): A list of documents.
    
    Returns:
    pandas.DataFrame: A DataFrame with words as columns and documents as rows, containing the TF-IDF scores.
    """
    # Initialize the TfidfVectorizer
    vectorizer = TfidfVectorizer(tokenizer=word_tokenize)
    
    # Fit and transform the documents
    tfidf_matrix = vectorizer.fit_transform(documents)
    
    # Convert the matrix to a DataFrame
    tfidf_df = pd.DataFrame(tfidf_matrix.toarray(), columns=vectorizer.get_feature_names_out())
    
    return tfidf_df
documents = [
    "The quick brown fox jumps over the lazy dog",
    "The dog barked at the fox",
    "The fox was quick and the dog was lazy"
]