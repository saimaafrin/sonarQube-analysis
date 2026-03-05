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
    texts (list of str): A list of text documents.
    
    Returns:
    pd.DataFrame: A DataFrame where rows represent documents and columns represent unique terms;
                 cell values indicate the frequency of a term in a document.
    """
    # Preprocess the texts
    processed_texts = []
    for text in texts:
        # Remove non-alphanumeric characters
        text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        text = text.lower()
        # Split into words
        words = text.split()
        # Remove stop words
        words = [word for word in words if word not in STOPWORDS]
        # Join words back into a single string
        processed_texts.append(' '.join(words))
    
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    
    # Fit and transform the processed texts
    dtm = vectorizer.fit_transform(processed_texts)
    
    # Convert the DTM to a DataFrame
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    
    return dtm_df
texts = [
    "Hello world, this is a test.",
    "This is another test, with some more words.",
    "Python is great for data science and machine learning."
]