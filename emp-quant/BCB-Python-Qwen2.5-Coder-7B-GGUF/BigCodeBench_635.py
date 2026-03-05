
# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

def task_func(text, n=2):
    # Define stopwords
    stop_words = set(stopwords.words('english'))
    
    # Remove duplicate consecutive words
    text = re.sub(r'\b(\w+)\b.*\b\1\b', r'\1', text)
    
    # Tokenize the text
    words = text.split()
    
    # Filter out stopwords
    words = [word for word in words if word not in stop_words]
    
    # Create a co-occurrence matrix
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(words)
    co_occurrence_matrix = (X.T * X).toarray()
    
    # Create a DataFrame for the co-occurrence matrix
    df = pd.DataFrame(co_occurrence_matrix, columns=vectorizer.get_feature_names_out(), index=vectorizer.get_feature_names_out())
    
    # Plot the co-occurrence matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    cax = ax.matshow(df, interpolation='nearest', cmap='Blues')
    fig.colorbar(cax)
    ax.set_xticks(np.arange(len(df.columns)))
    ax.set_yticks(np.arange(len(df.index)))
    ax.set_xticklabels(df.columns, rotation=90)
    ax.set_yticklabels(df.index)
    ax.set_title('Co-occurrence Matrix')
    
    return df, ax