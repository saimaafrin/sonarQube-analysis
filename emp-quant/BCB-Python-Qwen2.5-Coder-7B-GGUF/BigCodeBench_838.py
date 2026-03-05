
import re
from nltk.stem import PorterStemmer

def task_func(text_series):
    # Initialize the PorterStemmer
    stemmer = PorterStemmer()
    
    # Define a function to clean and stem each text
    def clean_and_stem(text):
        # Convert to lowercase
        text = text.lower()
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r'[^a-z0-9 ]', '', text)
        # Remove punctuation
        text = re.sub(r'[^\w\s]', '', text)
        # Split the text into words
        words = text.split()
        # Stem each word
        stemmed_words = [stemmer.stem(word) for word in words]
        # Join the stemmed words back into a single string
        return ' '.join(stemmed_words)
    
    # Apply the cleaning and stemming function to each element in the series
    cleaned_stemmed_series = text_series.apply(clean_and_stem)
    
    return cleaned_stemmed_series