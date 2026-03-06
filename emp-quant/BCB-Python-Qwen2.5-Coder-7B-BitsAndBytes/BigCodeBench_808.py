
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from textblob import TextBlob

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Remove stopwords
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Join the words back into a single string
    processed_text = ' '.join(filtered_words)
    
    # Analyze the sentiment using TextBlob
    blob = TextBlob(processed_text)
    sentiment = blob.sentiment
    
    return f"Sentiment: {sentiment}"