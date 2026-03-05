
import pandas as pd
import re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    # Split the text into sentences
    sentences = re.split(r'\.\s*', text)

    # Create a CountVectorizer object
    vectorizer = CountVectorizer()

    # Fit and transform the vectorizer to the sentences
    X = vectorizer.fit_transform(sentences)

    # Create a DataFrame with the document-term matrix
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())

    return df