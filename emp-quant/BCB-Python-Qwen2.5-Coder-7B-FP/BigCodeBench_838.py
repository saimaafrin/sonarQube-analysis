import re
from nltk.stem import PorterStemmer
def task_func(text_series):
    """
    Process a pandas Series of text data by lowercasing all letters, removing non-alphanumeric characters (except spaces),
    removing punctuation, and stemming each word to its root form.
    
    Args:
    text_series (pandas.Series): A pandas Series containing text data.
    
    Returns:
    pandas.Series: A Series where each string has been processed to remove non-alphanumeric characters,
    punctuation, converted to lowercase, and where each word has been stemmed.
    """
    ps = PorterStemmer()
    
    def process_text(text):
        # Lowercase the text
        text = text.lower()
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r'[^a-z0-9 ]', '', text)
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        # Split the text into words
        words = text.split()
        # Stem each word
        stemmed_words = [ps.stem(word) for word in words]
        # Join the stemmed words back into a single string
        return ' '.join(stemmed_words)
    
    # Apply the processing function to each element in the Series
    processed_series = text_series.apply(process_text)
    return processed_series