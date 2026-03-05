from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
def task_func(documents):
    """
    Calculate the TF-IDF score of the words in a list of documents.
    :param documents: A list of documents, where each document is a string.
    :return: A pandas.DataFrame with words as columns and documents as rows, containing the TF-IDF scores.
    """
    # Tokenize the documents
    documents_tokenized = [word_tokenize(doc) for doc in documents]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the documents
    vectorizer.fit(documents_tokenized)

    # Transform the documents
    documents_tfidf = vectorizer.transform(documents_tokenized)

    # Create a DataFrame with words as columns and documents as rows
    df = pd.DataFrame(documents_tfidf.toarray(), columns=vectorizer.get_feature_names())

    # Return the DataFrame
    return df
documents = ['This is a test document.', 'This is another test document.', 'This is a third test document.']