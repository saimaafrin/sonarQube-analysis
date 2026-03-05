import nltk
import re
from collections import Counter
STOPWORDS = nltk.corpus.stopwords.words('english')
def task_func(text):
    # Download necessary NLTK data
    nltk.download('stopwords')
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Split text into words
    words = text.split()
    
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    
    # Calculate frequency of each word
    word_freq = Counter(words)
    
    return word_freq