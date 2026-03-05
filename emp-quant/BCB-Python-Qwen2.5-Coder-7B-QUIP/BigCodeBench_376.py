
import nltk
import re
from collections import Counter
from nltk.corpus import stopwords
nltk.download('stopwords')
# Constants
STOPWORDS = set(stopwords.words('english'))

def task_func(text):
    # Function to clean and process the text
    def clean_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        # Remove stopwords
        words = [word for word in text.split() if word not in STOPWORDS]
        return words

    # Clean the input text
    words = clean_text(text)
    # Calculate the frequency of each word
    word_freq = Counter(words)
    return dict(word_freq)