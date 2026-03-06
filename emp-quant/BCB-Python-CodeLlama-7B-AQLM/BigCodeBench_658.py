import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(texts):
    """
    Creates a document-term matrix (DTM) from a list of text documents using CountVectorizer from Scikit-learn.
    Texts are preprocessed by removing non-alphanumeric characters (excluding spaces),
    converting to lowercase, and excluding English stop words defined in NLTK.

    Parameters:
    - texts (list of str): The list of text documents to convert into a DTM.

    Returns:
    - pd.DataFrame: A DataFrame where rows represent documents and columns represent unique terms;
                    cell values indicate the frequency of a term in a document.

    Requirements:
    - re
    - nltk
    - pandas
    - sklearn.feature_extraction.text

    Example:
    >>> texts = ["Hello, world!", "Machine learning is great.", "Python is my favorite programming language."]
    >>> dtm = task_func(texts)
    """
    # Create a list of preprocessed texts
    preprocessed_texts = []
    for text in texts:
        # Remove non-alphanumeric characters (excluding spaces)
        text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        text = text.lower()
        # Remove English stop words
        text = text.split()
        text = [word for word in text if word not in STOPWORDS]
        text = ' '.join(text)
        preprocessed_texts.append(text)

    # Create a CountVectorizer object
    vectorizer = CountVectorizer()

    # Create a DTM from the preprocessed texts
    dtm = vectorizer.fit_transform(preprocessed_texts)

    # Create a DataFrame from the DTM
    df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names())

    return df