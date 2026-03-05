import re
from collections import Counter
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    # Download the stopwords if not already downloaded
    stopwords.download('english')
    
    # Normalize the text to lower case
    text = text.lower()
    
    # Use regular expression to find words
    words = re.findall(r'\b\w+\b', text)
    
    # Get the list of English stopwords
    stop_words = set(stopwords.words('english'))
    
    # Filter out the stop words
    non_stop_words = [word for word in words if word not in stop_words]
    
    # Count the occurrences of each non-stop word
    word_count = Counter(non_stop_words)
    
    return dict(word_count)