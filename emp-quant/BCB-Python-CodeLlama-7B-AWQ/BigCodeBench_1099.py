import re
from collections import Counter
PREDEFINED_STOPWORDS = {
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", 
    "yourself", "yourselves", "he", "him", "his", "himself", "she", "her", "hers", 
    "herself", "it", "its", "itself", "they", "them", "their", "theirs", "themselves", 
    "what", "which", "who", "whom", "this", "that", "these", "those", "am", "is", "are", 
    "was", "were", "be", "been", "being", "have", "has", "had", "having", "do", "does", 
    "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", 
    "while", "of", "at", "by", "for", "with", "about", "against", "between", "into", 
    "through", "during", "before", "after", "above", "below", "to", "from", "up", "down", 
    "in", "out", "on", "off", "over", "under", "again", "further", "then", "once", "more"
}
def task_func(text):
    """
    Count the stopwords found in the text after you have removed URLs.
    Note that: Valid url is start with http or https
    The capitilization need to macth the stopwords
    """
    # Remove URLs
    text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", text)

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Convert to lowercase
    text = text.lower()

    # Split text into words
    words = text.split()

    # Create a counter for the words
    counter = Counter(words)

    # Filter out stopwords
    filtered_words = [word for word in words if word.lower() in PREDEFINED_STOPWORDS]

    # Create a new counter for the filtered words
    filtered_counter = Counter(filtered_words)

    # Return the list of tuples
    return [(word, count) for word, count in filtered_counter.items()]
text = "This is a sample text with http://www.example.com and https://www.example.com URLs and punctuation. The quick brown fox jumps over the lazy dog."