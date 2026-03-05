
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    # Tokenize the text
    tokens = re.split(r'\.', text)

    # Create a document-term matrix
    vectorizer = CountVectorizer(ngram_range=(1, 2))
    matrix = vectorizer.fit_transform(tokens)

    # Create a DataFrame from the matrix
    df = pd.DataFrame(matrix, columns=vectorizer.get_feature_names())

    return df