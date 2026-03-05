import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]
def task_func(file_path, save_path=None):
    # Read the input file
    df = pd.read_csv(file_path)
    # Check if the input file is empty or contains only stop words
    if df.shape[0] == 0 or df['text'].apply(lambda x: all(word in STOP_WORDS for word in x.split())).all():
        print("No valid words found in the input file.")
        return None
    # Perform text vectorization
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    X = vectorizer.fit_transform(df['text'])
    # Create a histogram of the ten most common words
    plt.figure(figsize=(10, 6))
    plt.bar(vectorizer.get_feature_names(), X.sum(axis=0))
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.title("Histogram of the ten most common words")
    if save_path:
        plt.savefig(save_path)
    else:
        plt.show()
    return plt.gca()