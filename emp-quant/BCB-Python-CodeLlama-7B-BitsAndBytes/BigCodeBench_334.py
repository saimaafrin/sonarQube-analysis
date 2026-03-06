
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd

def task_func(documents):
    # Tokenize the documents
    documents = [word_tokenize(doc) for doc in documents]

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the documents
    X = vectorizer.fit_transform(documents)

    # Convert the TF-IDF scores to a DataFrame
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())

    return df

df = task_func(documents)
print(df)