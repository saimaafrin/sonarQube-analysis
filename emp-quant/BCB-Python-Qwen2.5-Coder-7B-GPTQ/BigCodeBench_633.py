import re
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    # Define a set of common English stopwords
    common_stopwords = set(stopwords.words('english'))
    
    # Use regular expression to find words and convert them to lowercase
    words = re.findall(r'\b\w+\b', text.lower())
    
    # Filter out stopwords and duplicates
    filtered_words = [word for word in words if word not in common_stopwords]
    
    # Create a frequency distribution of the remaining words
    frequency_distribution = {}
    for word in filtered_words:
        if word in frequency_distribution:
            frequency_distribution[word] += 1
        else:
            frequency_distribution[word] = 1
    
    return frequency_distribution