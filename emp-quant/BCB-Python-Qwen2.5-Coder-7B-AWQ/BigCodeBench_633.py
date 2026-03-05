import re
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    # Manually defined set of common English stopwords
    custom_stopwords = set(['the', 'is', 'at', 'on', 'in', 'and', 'or', 'but', 'for', 'not', 'a', 'an'])
    
    # Combine nltk stopwords with custom stopwords
    all_stopwords = set(stopwords.words('english')).union(custom_stopwords)
    
    # Tokenize the text and remove stopwords
    words = re.findall(r'\b\w+\b', text.lower())
    filtered_words = [word for word in words if word not in all_stopwords]
    
    # Create frequency distribution
    frequency_distribution = {}
    for word in filtered_words:
        if word in frequency_distribution:
            frequency_distribution[word] += 1
        else:
            frequency_distribution[word] = 1
    
    return frequency_distribution