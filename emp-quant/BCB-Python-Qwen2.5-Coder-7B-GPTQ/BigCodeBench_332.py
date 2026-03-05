import re
from collections import Counter
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Remove stop words
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word not in stop_words]
    
    # Count the occurrences of each word
    word_count = Counter(filtered_words)
    
    return dict(word_count)
text = "This is a test. This test is only a test."