
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
    text = re.sub(r'\b(\w+)\s+\1\b', r'\1', text)
    
    # Tokenize the text
    words = text.split()
    
    # Filter out stopwords
    words = [word for word in words if word not in stop_words]
    
    # Create a CountVectorizer object
    vectorizer = CountVectorizer()
    
    # Fit and transform the words
    X = vectorizer.fit_transform(words)
    
    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Create a square co-occurrence matrix
    co_occurrence_matrix = X.T.dot(X)
    
    # Convert the co-occurrence matrix to a DataFrame
    co_occurrence_df = pd.DataFrame(co_occurrence_matrix, index=feature_names, columns=feature_names)
    
    # Plot the co-occurrence matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(co_occurrence_df, cmap='hot', interpolation='nearest')
    ax.set_xticks(np.arange(len(feature_names)))
    ax.set_yticks(np.arange(len(feature_names)))
    ax.set_xticklabels(feature_names, rotation=90)
    ax.set_yticklabels(feature_names)
    ax.set_title('Co-occurrence Matrix')
    
    return (co_occurrence_df, ax)