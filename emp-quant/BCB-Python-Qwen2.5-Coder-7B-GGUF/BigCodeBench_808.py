
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
    
    # Tokenize the text
    tokens = cleaned_text.split()
    
    # Remove stopwords
    filtered_tokens = [token for token in tokens if token not in STOPWORDS]
    
    # Reconstruct the text
    cleaned_text = ' '.join(filtered_tokens)
    
    # Analyze sentiment using TextBlob
    blob = TextBlob(cleaned_text)
    sentiment = blob.sentiment
    
    # Output the sentiment
    print(f"Sentiment: {sentiment}")