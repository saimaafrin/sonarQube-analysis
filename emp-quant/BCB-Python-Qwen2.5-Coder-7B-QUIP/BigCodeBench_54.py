
import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    # Split the text into sentences using regex to handle periods
    sentences = re.split(r'\.|\n', text)
    # Filter out empty sentences
    sentences = [sentence for sentence in sentences if sentence.strip()]
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    # Fit and transform the sentences
    X = vectorizer.fit_transform(sentences)
    
    # Convert the result to a DataFrame
    df = pd.DataFrame(X.toarray(), columns=vectorizer.get_feature_names_out())
    
    return df