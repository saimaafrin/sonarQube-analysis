import re
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    # Manually defined set of common English stopwords
    common_stopwords = set(['the', 'and', 'is', 'in', 'it', 'of', 'to', 'that', 'with', 'for', 'on', 'at', 'as', 'by', 'from', 'this', 'an', 'or', 'but', 'not', 'if', 'so', 'because', 'while', 'how', 'when', 'where', 'who', 'what', 'which', 'why', 'up', 'down', 'left', 'right', 'front', 'back', 'inside', 'outside', 'above', 'below', 'under', 'over', 'through', 'across', 'behind', 'between', 'among', 'around', 'above', 'below', 'under', 'over', 'through', 'across', 'behind', 'between', 'among', 'around'])

    # Tokenize the text into words
    words = re.findall(r'\b\w+\b', text.lower())

    # Remove stopwords and duplicates
    filtered_words = list(set(word for word in words if word not in stopwords.words('english') and word not in common_stopwords))

    # Create a frequency distribution of the remaining words
    frequency_distribution = {word: filtered_words.count(word) for word in filtered_words}

    return frequency_distribution