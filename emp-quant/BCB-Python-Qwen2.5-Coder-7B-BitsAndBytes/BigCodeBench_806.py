
import re
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
from collections import Counter

# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text, n=2):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Remove stopwords
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Generate n-grams
    n_grams = [' '.join(filtered_words[i:i+n]) for i in range(len(filtered_words) - n + 1)]
    
    # Count the occurrences of each n-gram
    n_gram_counts = Counter(n_grams)
    
    return n_gram_counts