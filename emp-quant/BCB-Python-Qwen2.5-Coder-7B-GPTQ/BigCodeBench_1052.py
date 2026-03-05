import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]
def task_func(file_path, save_path=None):
    # Load the dataset
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found.")
        return None

    # Check if the DataFrame is empty
    if df.empty:
        print("The dataset is empty.")
        return None

    # Extract text data
    text_data = df['text'].dropna().values

    # Initialize CountVectorizer
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)

    # Fit and transform the text data
    word_counts = vectorizer.fit_transform(text_data)

    # Get feature names and their counts
    feature_names = vectorizer.get_feature_names_out()
    counts = word_counts.sum(axis=0).A1

    # Create a dictionary of word counts
    word_count_dict = dict(zip(feature_names, counts))

    # Sort the dictionary by count in descending order
    sorted_word_count_dict = dict(sorted(word_count_dict.items(), key=lambda item: item[1], reverse=True))

    # Get the top 10 words and their counts
    top_10_words = list(sorted_word_count_dict.keys())[:10]
    top_10_counts = list(sorted_word_count_dict.values())[:10]

    # Create a histogram of the top 10 words
    plt.figure(figsize=(10, 5))
    plt.bar(top_10_words, top_10_counts, color='blue')
    plt.xlabel('Words')
    plt.ylabel('Frequency')
    plt.title('Top 10 Most Common Words')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        plt.close()
        return None

    # Return the matplotlib Axes object if save_path is not provided
    return plt.gca()