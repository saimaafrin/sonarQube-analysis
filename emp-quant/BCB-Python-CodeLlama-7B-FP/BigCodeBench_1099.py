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
    Note that: Valid url is start with http or https The capitilization need to macth the stopwords
    The function should output with:
        list: A list of tuples where each tuple contains a word and its frequency.
    """
    # Remove URLs
    text = re.sub(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+", "", text)

    # Remove punctuation
    text = re.sub(r"[^\w\s]", "", text)

    # Convert to lowercase
    text = text.lower()

    # Tokenize the text
    tokens = text.split()

    # Create a counter for the stopwords
    counter = Counter()

    # Iterate over the tokens and count the stopwords
    for token in tokens:
        if token in PREDEFINED_STOPWORDS:
            counter[token] += 1

    # Return the counter
    return counter.most_common()
text = "This is a sample text with some http://www.example.com URLs and punctuation. The quick brown fox jumps over the lazy dog."