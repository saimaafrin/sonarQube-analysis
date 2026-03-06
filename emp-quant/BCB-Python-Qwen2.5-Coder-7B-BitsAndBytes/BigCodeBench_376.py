
import nltk
import re
from collections import Counter

# Ensure necessary NLTK data is downloaded
nltk.download('stopwords')

# Constants
STOPWORDS = set(nltk.corpus.stopwords.words('english'))

def task_func(text):
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split the text into words
    words = text.split()
    
    # Filter out stopwords
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Calculate the frequency of each word
    word_frequency = Counter(filtered_words)
    
    return word_frequency