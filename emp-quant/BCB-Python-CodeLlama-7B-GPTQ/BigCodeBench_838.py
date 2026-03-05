import re
from nltk.stem import PorterStemmer
def task_func(text_series):
    """
    Process a pandas Series of text data by lowercasing all letters, removing non-alphanumeric characters (except spaces), removing punctuation, and stemming each word to its root form.
    Stemming is done using the NLTK's PorterStemmer, which applies a series of rules to find the stem of each word.
    The function should output with:
        pandas.Series: A Series where each string has been processed to remove non-alphanumeric characters,
        punctuation, converted to lowercase, and where each word has been stemmed.
    """
    # Create a list of words from the text_series
    words = text_series.str.split()

    # Create a list of stemmed words
    stemmed_words = []
    for word in words:
        # Remove non-alphanumeric characters (except spaces)
        word = re.sub(r'[^a-zA-Z\s]', '', word)
        # Remove punctuation
        word = re.sub(r'[^\w\s]', '', word)
        # Convert to lowercase
        word = word.lower()
        # Stem the word
        stemmer = PorterStemmer()
        stemmed_word = stemmer.stem(word)
        stemmed_words.append(stemmed_word)

    # Create a new pandas Series with the stemmed words
    stemmed_series = pd.Series(stemmed_words)

    return stemmed_series
text_series = pd.Series(['This is a test sentence.', 'This is another test sentence.'])