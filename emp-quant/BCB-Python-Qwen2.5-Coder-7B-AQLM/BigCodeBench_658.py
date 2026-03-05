
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
    # Preprocess the texts
    preprocessed_texts = []
    for text in texts:
        # Remove non-alphanumeric characters
        text = ALPHANUMERIC.sub(' ', text)
        # Convert to lowercase
        text = text.lower()
        # Remove English stop words
        text = ' '.join(word for word in text.split() if word not in STOPWORDS)
        preprocessed_texts.append(text)
    
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    
    # Fit and transform the preprocessed texts
    X = vectorizer.fit_transform(preprocessed_texts)
    
    # Convert the result to a DataFrame
    DTM = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    
    return DTM