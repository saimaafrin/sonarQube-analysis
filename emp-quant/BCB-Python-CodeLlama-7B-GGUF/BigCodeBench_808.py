
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
# Constants
STOPWORDS = set(stopwords.words('english'))
def task_func(text):
    # Remove duplicate and stopwords from the text
    text = re.sub(r'\b\w+\b', '', text)
    text = ' '.join([word for word in text.split() if word.lower() not in STOPWORDS])
    # Analyze the sentiment of the text
    sentiment = TextBlob(text).sentiment
    return sentiment