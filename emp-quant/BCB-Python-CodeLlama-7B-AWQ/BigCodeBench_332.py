import re
from collections import Counter
from nltk.corpus import stopwords
def task_func(text: str) -> dict:
    """
    Count the number of non-stop words in a given text.

    Args:
        text (str): The text to be analyzed.

    Returns:
        dict: A dictionary with the words (as keys) and their counts (as values).
    """
    # Remove punctuation and convert to lowercase
    text = re.sub(r'[^a-zA-Z]', '', text.lower())

    # Tokenize the text
    tokens = text.split()

    # Remove stop words
    stop_words = set(stopwords.words('english'))
    tokens = [word for word in tokens if word not in stop_words]

    # Count the number of non-stop words
    counts = Counter(tokens)

    # Return the dictionary of non-stop words and their counts
    return counts
text = "This is a sample text with some stop words like 'the' and 'a'."