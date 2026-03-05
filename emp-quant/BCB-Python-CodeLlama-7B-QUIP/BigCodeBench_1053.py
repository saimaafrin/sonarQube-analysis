
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]
def task_func(file_path, save_path=None):
    # Read the CSV file
    df = pd.read_csv(file_path)
    # Remove the header if it exists
    if "Text" in df.columns:
        df = df.iloc[:, 1:]
    # Convert the text to lowercase
    df["Text"] = df["Text"].str.lower()
    # Tokenize the text
    df["Text"] = df["Text"].str.split()
    # Remove stopwords
    df["Text"] = df["Text"].apply(lambda x: [word for word in x if word not in STOP_WORDS])
    # Create a histogram of the top ten most common words
    top_ten = df["Text"].str.get(0).value_counts().head(10)
    # Plot the histogram
    plt.figure(figsize=(8, 6))
    plt.bar(top_ten.index, top_ten.values, color="blue")
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.title("Top Ten Most Common Words")
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    return None