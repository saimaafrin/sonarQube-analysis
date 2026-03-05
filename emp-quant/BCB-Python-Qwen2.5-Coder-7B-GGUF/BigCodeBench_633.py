
import re
from nltk.corpus import stopwords

def task_func(text: str) -> dict:
    # Manually defined set of common English stopwords
    common_stopwords = set(['the', 'and', 'is', 'in', 'of', 'to', 'a', 'that', 'it', 'for', 'on', 'with', 'as', 'at', 'by', 'from', 'this', 'an', 'be', 'or', 'not', 'have', 'but', 'if', 'will', 'can', 'will', 'may', 'must', 'should', 'can', 'could', 'would', 'may', 'might', 'must', 'need', 'dare', 'ought', 'used', 'would', 'shall', 'can', 'could', 'would', 'may', 'might', 'must', 'need', 'dare', 'ought', 'used', 'would', 'shall'])

    # Tokenize the text and remove non-alphabetic characters
    words = re.findall(r'\b\w+\b', text.lower())

    # Remove stopwords and common English stopwords
    filtered_words = [word for word in words if word not in stopwords.words('english') and word not in common_stopwords]

    # Create a frequency distribution of the remaining words
    frequency_distribution = {}
    for word in filtered_words:
        if word in frequency_distribution:
            frequency_distribution[word] += 1
        else:
            frequency_distribution[word] = 1

    return frequency_distribution