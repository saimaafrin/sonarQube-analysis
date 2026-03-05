
import re
from nltk.corpus import stopwords
from collections import Counter

# Download the stopwords corpus if not already downloaded
try:
    stopwords corpus
except:
    nltk.download('stopwords')

def task_func(text: str) -> dict:
    # Define a manually defined set of common English stopwords
    custom_stopwords = {'the', 'is', 'at', 'and', 'in', 'a', 'to', 'of', 'with', 'for', 'on', 'that', 'this', 'it', 'by', 'from', 'or', 'as', 'at', 'to', 'in', 'a', 'to', 'of', 'with', 'for', 'on', 'that', 'this', 'it', 'by', 'from', 'or', 'as'}

    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text)

    # Remove stopwords and custom stopwords
    filtered_words = [word for word in words if word.lower() not in stopwords.words('english') and word.lower() not in custom_stopwords]

    # Convert the list of words to a frequency distribution
    word_freq = Counter(filtered_words)

    return dict(word_freq)