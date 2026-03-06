
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    # Read the CSV file
    df = pd.read_csv(file_path)

    # Create a CountVectorizer object with the stop words
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)

    # Fit and transform the data
    X = vectorizer.fit_transform(df['text'])

    # Get the top 10 most common words
    top_words = X.sum(axis=0).sort_values(ascending=False)[:10].index

    # Create a histogram of the top 10 words
    plt.bar(top_words, X[top_words].sum(axis=0))

    # Save the plot if a save path is provided
    if save_path:
        plt.savefig(save_path)
        return None

    # Display the plot and return the matplotlib Axes object
    plt.show()
    return plt.gca()