import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]
def task_func(file_path, save_path=None):
    """
    This function processes a text dataset from a CSV file, performs text vectorization while excluding specific stopwords, and creates a histogram of the ten most common words.
    The function is robust to different input scenarios, such as empty data or data containing only stopwords.
    The function should output with:
        matplotlib Axes object: If save_path is not provided and valid words are found in the input, the function
        displays the histogram plot and returns the matplotlib Axes object.
        None: In two scenarios:
        1. If save_path is provided, saves the plot to the specified location and returns None.
        2. If the input file is empty or contains only stop words, prints a message and returns None.
    """
    # Read the input file
    df = pd.read_csv(file_path)

    # Check if the input file is empty or contains only stopwords
    if df.empty or (df['text'].str.lower().str.split().str.len() == 1).all():
        print("The input file is empty or contains only stopwords.")
        return None

    # Perform text vectorization
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    X = vectorizer.fit_transform(df['text'])

    # Create a histogram of the ten most common words
    word_counts = X.sum(axis=0)
    top_words = word_counts.sort_values(ascending=False).head(10)
    plt.bar(top_words.index, top_words.values)

    # Save the plot to the specified location
    if save_path:
        plt.savefig(save_path)
        return None

    # Display the plot and return the matplotlib Axes object
    plt.show()
    return plt.gca()
file_path = "data.csv"
save_path = "output.png"