
import re
from nltk.stem import PorterStemmer

def task_func(text_series):
    # Initialize the stemmer
    stemmer = PorterStemmer()
    
    # Define a function to clean and stem each word
    def clean_and_stem(word):
        # Remove non-alphanumeric characters except spaces
        word = re.sub(r'[^a-zA-Z0-9 ]', '', word)
        # Convert to lowercase
        word = word.lower()
        # Stem the word
        word = stemmer.stem(word)
        return word
    
    # Apply the cleaning and stemming to each element in the Series
    cleaned_stemmed_series = text_series.apply(clean_and_stem)
    
    return cleaned_stemmed_series