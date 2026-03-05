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

    # Create a DataFrame with the matrix
    df = pd.DataFrame(matrix.toarray(), columns=vectorizer.get_feature_names())

    return df
text = "This is a sentence. This is another sentence. This is a third sentence."