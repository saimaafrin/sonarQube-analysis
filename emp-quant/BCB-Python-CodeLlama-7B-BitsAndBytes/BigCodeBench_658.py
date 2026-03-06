
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
    # Preprocess the text data by removing non-alphanumeric characters and converting to lowercase
    texts = [re.sub(ALPHANUMERIC, ' ', text.lower()) for text in texts]
    # Remove English stop words
    texts = [text for text in texts if text not in STOPWORDS]
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    # Fit and transform the data
    X = vectorizer.fit_transform(texts)
    # Convert the sparse matrix to a DataFrame
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())
    return df