from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
def task_func(documents):
    """
    Calculate the TF-IDF score of the words in a list of documents.
    :param documents: A list of documents
    :return: A pandas.DataFrame with words as columns and documents as rows, containing the TF-IDF scores.
    """
    # Tokenize the documents
    documents = [word_tokenize(doc) for doc in documents]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the documents
    X = vectorizer.fit_transform(documents)

    # Create a DataFrame with words as columns and documents as rows
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())

    # Return the DataFrame
    return df
documents = [
    "This is the first document.",
    "This is the second document.",
    "This is the third document.",
]