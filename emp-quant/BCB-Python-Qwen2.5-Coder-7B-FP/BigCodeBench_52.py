import pandas as pd
import regex as re
STOPWORDS = ["a", "an", "the", "in", "is", "are"]
def task_func(text):
    # Remove non-alphabetic characters and convert to lowercase
    cleaned_text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    
    # Split the text into words
    words = cleaned_text.split()
    
    # Filter out stopwords
    filtered_words = [word for word in words if word not in STOPWORDS]
    
    # Count the frequency of each word
    word_counts = pd.Series(filtered_words).value_counts()
    
    return word_counts