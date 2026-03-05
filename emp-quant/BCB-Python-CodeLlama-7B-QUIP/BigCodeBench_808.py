
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
# Constants
STOPWORDS = set(stopwords.words('english'))
def task_func(text):
    # Remove stopwords
    text = re.sub(r'\b' + '|'.join(STOPWORDS) + r'\b', '', text)
    # Remove duplicate words
    text = re.sub(r'\b\w+\b', '', text)
    # Analyze sentiment
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment