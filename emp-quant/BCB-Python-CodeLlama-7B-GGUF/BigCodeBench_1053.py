
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]
def task_func(file_path, save_path=None):
    # Read the CSV file
    df = pd.read_csv(file_path)
    # Extract the text column
    text_column = df['Text']
    # Create a CountVectorizer object
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    # Fit and transform the text data
    X = vectorizer.fit_transform(text_column)
    # Get the frequency of the top ten most common words
    top_ten_words = X.sum(axis=0).argsort()[-10:][::-1]
    # Create a histogram of the frequency of the top ten most common words
    plt.bar(top_ten_words, X[top_ten_words].sum(axis=0))
    # Set the title and labels
    plt.title('Histogram of Top Ten Most Common Words')
    plt.xlabel('Word')
    plt.ylabel('Frequency')
    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
    # Return the Axes object if save_path is not provided
    else:
        return plt.gca()