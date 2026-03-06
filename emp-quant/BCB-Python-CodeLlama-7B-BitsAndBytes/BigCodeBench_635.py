
# Importing the required libraries
import re
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# Define the function to analyze the text string and generate the co-occurrence matrix
def task_func(text, n=2):
    # Remove duplicate consecutive words and stopwords
    text = re.sub(r'\b\w+\b', '', text)
    text = ' '.join(text.split())
    text = ' '.join(text.split())
    stop_words = set(stopwords.words('english'))
    text = [word for word in text.split() if word not in stop_words]

    # Generate the co-occurrence matrix
    vectorizer = CountVectorizer(ngram_range=(1, n))
    X = vectorizer.fit_transform(text)
    co_occurrence_matrix = X.toarray()

    # Plot the co-occurrence matrix
    fig, ax = plt.subplots(figsize=(10, 10))
    ax.imshow(co_occurrence_matrix, cmap='gray')
    ax.set_title('Co-occurrence Matrix')
    ax.set_xlabel('Word 1')
    ax.set_ylabel('Word 2')
    ax.set_xticks(np.arange(co_occurrence_matrix.shape[0]))
    ax.set_yticks(np.arange(co_occurrence_matrix.shape[1]))
    ax.set_xticklabels(vectorizer.get_feature_names())
    ax.set_yticklabels(vectorizer.get_feature_names())
    plt.show()

    # Return the co-occurrence matrix and the plot object
    return co_occurrence_matrix, ax