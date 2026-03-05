
import re
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def task_func(df):
    # Check if the DataFrame contains 'Title' and 'Content' columns
    if 'Title' not in df.columns or 'Content' not in df.columns:
        return plt.figure()

    # Extract the titles and content from the DataFrame
    titles = df['Title']
    content = df['Content']

    # Create a TfidfVectorizer object
    vectorizer = TfidfVectorizer()

    # Fit and transform the vectorizer to the content
    X = vectorizer.fit_transform(content)

    # Extract the TF-IDF scores for the words in the content
    scores = X.toarray()

    # Filter the scores to only include the words in the titles
    filtered_scores = scores[np.array(titles) != '']

    # Calculate the average TF-IDF score for each word in the titles
    average_scores = filtered_scores.mean(axis=0)

    # Create a bar plot of the TF-IDF scores
    plt.bar(average_scores.index, average_scores.values)

    # Set the y-axis label
    plt.ylabel('TF-IDF Score')

    # Set the x-axis ticks to display the feature names vertically
    plt.xticks(rotation=90)

    # Return the Axes object
    return plt.gca()