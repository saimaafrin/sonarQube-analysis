import re
import nltk
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
ALPHANUMERIC = re.compile('[\W_]+')
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(texts):
    # Preprocess the text data
    texts = [re.sub(ALPHANUMERIC, ' ', text.lower()) for text in texts]
    texts = [word for text in texts for word in text.split() if word.lower() not in STOPWORDS]

    # Create a CountVectorizer object
    vectorizer = CountVectorizer()

    # Fit and transform the data
    X = vectorizer.fit_transform(texts)

    # Create a DataFrame with the term-document matrix
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names())

    # Return the DataFrame
    return df
texts = ['This is a sample text.', 'This is another sample text.']