
import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer

# Ensure necessary NLTK resources are downloaded
nltk.download('stopwords')

# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')

# Load NLTK's list of English stop words
STOPWORDS = nltk.corpus.stopwords.words('english')

def preprocess_text(text):
    """Preprocesses the text by removing non-alphanumeric characters,
       converting to lowercase, and removing stop words."""
    # Remove non-alphanumeric characters
    text = ALPHANUMERIC.sub(' ', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize and remove stop words
    tokens = [word for word in text.split() if word not in STOPWORDS]
    return ' '.join(tokens)

def task_func(texts):
    """
    Creates a document-term matrix (DTM) from a list of text documents.

    Parameters:
    texts (list): A list of text documents.

    Returns:
    pd.DataFrame: A DataFrame representing the DTM.
    """
    # Preprocess each text in the list
    processed_texts = [preprocess_text(text) for text in texts]

    # Initialize CountVectorizer
    vectorizer = CountVectorizer()

    # Fit and transform the processed texts
    dtm = vectorizer.fit_transform(processed_texts)

    # Create a DataFrame from the DTM
    df_dtm = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())

    return df_dtm