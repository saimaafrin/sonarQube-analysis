import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
STOPWORDS = set(stopwords.words('english'))
def task_func(text):
    """
    Remove duplicate and stopwords from a string "text." Then, analyze the sentiment of the text using TextBlob.
    """
    # Remove duplicate words
    text = re.sub(r'\b\w+\b', '', text)
    # Remove stopwords
    text = re.sub(r'\b(?:{})\b'.format('|'.join(STOPWORDS)), '', text)
    # Analyze sentiment
    sentiment = TextBlob(text).sentiment
    return sentiment
text = "This is a test string with some duplicate and stopwords."