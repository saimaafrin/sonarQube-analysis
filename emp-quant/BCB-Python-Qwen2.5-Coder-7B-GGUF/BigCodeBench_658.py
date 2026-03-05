
import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
# Make sure to download NLTK stopwords
nltk.download('stopwords')
# Define a regex pattern for matching all non-alphanumeric characters
ALPHANUMERIC = re.compile('[\W_]+')
# Load NLTK's list of English stop words
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
    processed_texts = [ALPHANUMERIC.sub(' ', text).lower() for text in texts]
    processed_texts = [' '.join([word for word in text.split() if word not in STOPWORDS]) for text in processed_texts]
    
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    
    # Fit and transform the processed texts
    dtm = vectorizer.fit_transform(processed_texts)
    
    # Convert the DTM to a DataFrame
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    
    return dtm_df