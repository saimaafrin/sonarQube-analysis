import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(texts):
    """
    Creates a document-term matrix (DTM) from a list of text documents using CountVectorizer from Scikit-learn.
    Texts are preprocessed by removing non-alphanumeric characters (excluding spaces), converting to lowercase, and excluding English stop words defined in NLTK.
    The function should output with:
        pd.DataFrame: A DataFrame where rows represent documents and columns represent unique terms;
        cell values indicate the frequency of a term in a document.
    """
    # Preprocess texts
    texts = [re.sub(ALPHANUMERIC, ' ', text.lower()) for text in texts]
    texts = [word for text in texts for word in text.split() if word not in STOPWORDS]

    # Create DTM
    vectorizer = CountVectorizer()
    dtm = vectorizer.fit_transform(texts)

    # Convert to DataFrame
    df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names())

    return df
texts = ['This is a test document.', 'This is another test document.']