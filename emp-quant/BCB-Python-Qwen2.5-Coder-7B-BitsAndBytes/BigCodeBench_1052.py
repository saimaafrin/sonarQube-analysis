
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Constants
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
    
    # Extract the text column
    text_column = df['text']
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    
    # Fit and transform the text data
    X = vectorizer.fit_transform(text_column)
    
    # Get feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Sum up the counts for each word across all documents
    word_counts = X.sum(axis=0).A1
    
    # Create a dictionary of word counts
    word_dict = dict(zip(feature_names, word_counts))
    
    # Sort the dictionary by word count in descending order
    sorted_word_dict = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    
    # Get the top 10 most common words
    top_10_words = [word for word, count in sorted_word_dict[:10]]
    top_10_counts = [count for word, count in sorted_word_dict[:10]]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(top_10_words, top_10_counts)
    ax.set_xlabel('Words')
    ax.set_ylabel('Counts')
    ax.set_title('Top 10 Most Common Words')
    
    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        plt.close(fig)
        return None
    
    # Display the plot
    plt.show()
    return ax