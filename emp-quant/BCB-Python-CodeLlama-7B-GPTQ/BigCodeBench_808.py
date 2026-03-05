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
    text = re.sub(r'\b(\w+)\b', r'\1', text)

    # Remove stopwords
    text = ' '.join([word for word in text.split() if word.lower() not in STOPWORDS])

    # Analyze sentiment
    sentiment = TextBlob(text).sentiment

    return sentiment
text = "I love this movie! It's so great!"