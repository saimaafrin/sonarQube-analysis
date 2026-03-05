import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
STOPWORDS = set(stopwords.words('english'))
def task_func(text):
    # Remove non-alphabetic characters and convert to lowercase
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Tokenize the text
    words = text.split()
    
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    
    # Reconstruct the text without stopwords
    cleaned_text = ' '.join(words)
    
    # Analyze sentiment using TextBlob
    blob = TextBlob(cleaned_text)
    sentiment = blob.sentiment
    
    # Output the sentiment
    return f"Sentiment: {sentiment}"
text = "This is a sample text with some stopwords and duplicate words. Duplicate words should be removed."