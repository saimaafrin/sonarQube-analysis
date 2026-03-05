import re
from nltk.stem import PorterStemmer
def task_func(text_series):
    """
    Processes a pandas Series of text data by lowercasing all letters, removing non-alphanumeric characters (except spaces),
    removing punctuation, and stemming each word to its root form using NLTK's PorterStemmer.
    
    Parameters:
    text_series (pandas.Series): A pandas Series containing text data to be processed.
    
    Returns:
    pandas.Series: A Series with processed text data.
    """
    # Initialize PorterStemmer
    stemmer = PorterStemmer()
    
    # Define a function to process a single text string
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r'[^a-z0-9 ]', '', text)
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        # Split text into words
        words = text.split()
        # Stem each word
        stemmed_words = [stemmer.stem(word) for word in words]
        # Join stemmed words back into a single string
        return ' '.join(stemmed_words)
    
    # Apply the process_text function to each element in the Series
    processed_series = text_series.apply(process_text)
    
    return processed_series