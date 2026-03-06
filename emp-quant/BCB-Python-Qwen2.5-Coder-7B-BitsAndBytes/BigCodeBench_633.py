
import re
from nltk.corpus import stopwords

# Manually defined set of common English stopwords
custom_stopwords = {
    "the", "and", "is", "in", "it", "of", "to", "that", "with", "for", "on", "at", "by", "as", "an"
}

def task_func(text: str) -> dict:
    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Remove stopwords using both NLTK corpus and custom stopwords
    filtered_words = [word for word in words if word not in stopwords.words('english') and word not in custom_stopwords]
    
    # Create a frequency distribution of the remaining words
    from collections import Counter
    freq_dist = dict(Counter(filtered_words))
    
    return freq_dist