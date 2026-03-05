
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
    # Preprocess the texts by removing non-alphanumeric characters and converting to lowercase
    texts = [re.sub(ALPHANUMERIC, ' ', text).lower() for text in texts]
    # Remove stopwords
    texts = [word for word in texts if word not in STOPWORDS]
    # Create a document-term matrix (DTM) using CountVectorizer
    vectorizer = CountVectorizer(ngram_range=(1, 1))
    dtm = vectorizer.fit_transform(texts)
    # Return the DTM as a DataFrame
    return pd.DataFrame(dtm, columns=vectorizer.get_feature_names())