from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
def task_func(documents):
    """
    Calculate the TF-IDF score of the words in a list of documents.
    
    Parameters:
    - documents (list of str): A list of text documents.
    
    Returns:
    pandas.DataFrame: A DataFrame with words as columns and documents as rows, containing the TF-IDF scores.
    
    Requirements:
    - nltk.tokenize.word_tokenize
    - sklearn.feature_extraction.text.TfidfVectorizer
    - pandas
    
    Example:
    >>> docs = ['This is the first document.', 'This document is the second document.', 'And this is the third one.', 'Is this the first document?']
    >>> tfidf = task_func(docs)
    >>> print(tfidf.shape)
    (4, 11)
    """
    # Tokenize the documents
    documents = [word_tokenize(doc) for doc in documents]
    
    # Create a TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    
    # Fit the vectorizer to the documents
    vectorizer.fit(documents)
    
    # Transform the documents
    tfidf = vectorizer.transform(documents)
    
    # Create a DataFrame with the TF-IDF scores
    df = pd.DataFrame(tfidf.toarray(), columns=vectorizer.get_feature_names())
    
    # Return the DataFrame
    return df