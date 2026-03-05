
import nltk
import re
from collections import Counter
# Constants
STOPWORDS = nltk.corpus.stopwords.words('english')

def task_func(text):
    # Download necessary NLTK data
    nltk.download('stopwords')
    nltk.download('punkt')
    
    # Convert text to lowercase
    text = text.lower()
    
    # Remove punctuation using regex
    text = re.sub(r'[^\w\s]', '', text)
    
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    
    # Calculate the frequency of each word
    word_freq = Counter(words)
    
    return word_freq