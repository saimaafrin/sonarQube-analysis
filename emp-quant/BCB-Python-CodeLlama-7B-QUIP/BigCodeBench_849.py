
import re
from nltk.corpus import stopwords
from collections import Counter
STOPWORDS = set(stopwords.words('english'))
def task_func(input_string):
    # Remove punctuation and convert to lowercase
    input_string = re.sub(r'[^\w\s]', '', input_string).lower()
    # Tokenize the string into individual words
    words = re.split(r'\s+', input_string)
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    # Count the frequency of each word
    word_counts = Counter(words)
    return word_counts