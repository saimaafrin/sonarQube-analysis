
import re
from nltk.stem import PorterStemmer

def task_func(text_series):
    # Initialize the PorterStemmer
    stemmer = PorterStemmer()
    
    # Define a function to process each text item
    def process_text(text):
        # Convert to lowercase
        text = text.lower()
        
        # Remove non-alphanumeric characters except spaces
        text = re.sub(r'[^a-z0-9 ]', '', text)
        
        # Tokenize the text into words
        words = text.split()
        
        # Stem each word
        stemmed_words = [stemmer.stem(word) for word in words]
        
        # Join the stemmed words back into a single string
        return ' '.join(stemmed_words)
    
    # Apply the processing function to each element in the Series
    processed_series = text_series.apply(process_text)
    
    return processed_series