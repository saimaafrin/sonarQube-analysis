import re
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
STOPWORDS = set(stopwords.words('english'))
def task_func(text):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Tokenize the text
    tokens = cleaned_text.split()
    
    # Remove stopwords
    filtered_tokens = [word for word in tokens if word not in STOPWORDS]
    
    # Reconstruct the text
    cleaned_text = ' '.join(filtered_tokens)
    
    # Analyze sentiment using TextBlob
    blob = TextBlob(cleaned_text)
    sentiment = blob.sentiment
    
    return f"Sentiment: {sentiment}"