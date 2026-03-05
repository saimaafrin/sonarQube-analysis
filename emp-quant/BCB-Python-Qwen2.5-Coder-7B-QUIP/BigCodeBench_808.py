
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob
# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text):
    # Remove duplicate words
    words = text.split()
    unique_words = list(set(words))
    
    # Remove stopwords
    filtered_words = [word for word in unique_words if word not in STOPWORDS]
    
    # Reconstruct the text
    filtered_text = ' '.join(filtered_words)
    
    # Analyze sentiment
    analysis = TextBlob(filtered_text)
    sentiment = analysis.sentiment
    
    return f"Sentiment: {sentiment}"