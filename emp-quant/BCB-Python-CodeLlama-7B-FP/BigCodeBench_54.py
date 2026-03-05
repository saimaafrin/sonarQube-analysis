import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer
def task_func(text):
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()

    # Tokenize the text
    tokens = vectorizer.tokenize(text)

    # Remove empty sentences
    tokens = [token for token in tokens if token != ""]

    # Create a document-term matrix
    matrix = vectorizer.fit_transform(tokens)

    # Convert the matrix to a DataFrame
    df = pd.DataFrame(matrix.toarray(), columns=vectorizer.get_feature_names())

    return df
text = "This is a sample text. This is another sample text. This is a third sample text."