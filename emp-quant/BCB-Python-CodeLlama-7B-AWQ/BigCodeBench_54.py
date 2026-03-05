import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
def task_func(text):
    """
    Analyze a text by creating a document term matrix with CountVectorizer.
    The text contains several sentences, each separated by a period. Ignore empty sentences.
    The function should output with:
        DataFrame: A pandas DataFrame with the document-term matrix. Its column names should be adapted from the vectorizer feature names.
    """
    # Create a list of sentences
    sentences = re.split(r'\.', text)
    # Remove empty sentences
    sentences = [s for s in sentences if s.strip()]
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    # Fit the vectorizer to the sentences
    vectorizer.fit(sentences)
    # Create a document-term matrix
    matrix = vectorizer.transform(sentences)
    # Convert the matrix to a DataFrame
    df = pd.DataFrame(matrix.toarray(), columns=vectorizer.get_feature_names())
    return df
text = "This is a sample text. This is another sample text."