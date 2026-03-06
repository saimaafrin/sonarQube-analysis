
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def task_func(df):
    # Check if the DataFrame contains 'Title' and 'Content' columns
    if 'Title' not in df.columns or 'Content' not in df.columns:
        return plt.figure()

    # Extract the words from the titles and content
    titles = df['Title'].str.split()
    contents = df['Content'].str.split()

    # Create a list of all words in the titles and content
    words = titles + contents

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit the vectorizer to the words
    vectorizer.fit(words)

    # Transform the words into TF-IDF scores
    scores = vectorizer.transform(words)

    # Create a bar plot of the TF-IDF scores
    plt.bar(scores.get_feature_names(), scores.toarray().ravel())

    # Set the y-axis label
    plt.ylabel('TF-IDF Score')

    # Set the xticks to display the feature names vertically
    plt.xticks(rotation=90)

    # Return the Axes object
    return plt.gca()