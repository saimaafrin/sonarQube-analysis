import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(texts):
    """
    Creates a document-term matrix (DTM) from a list of text documents using CountVectorizer from Scikit-learn.
    
    Parameters:
    texts (list): A list of text documents.
    
    Returns:
    pd.DataFrame: A DataFrame where rows represent documents and columns represent unique terms;
                 cell values indicate the frequency of a term in a document.
    """
    # Preprocess the texts
    processed_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    processed_texts = [' '.join([word for word in text.split() if word not in STOPWORDS]) for text in processed_texts]
    
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    
    # Fit and transform the processed texts
    X = vectorizer.fit_transform(processed_texts)
    
    # Create a DataFrame from the transformed data
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    
    return df
texts = [
    "Hello, world! This is a test.",
    "Another example, with some words.",
    "More text, for demonstration purposes."
]