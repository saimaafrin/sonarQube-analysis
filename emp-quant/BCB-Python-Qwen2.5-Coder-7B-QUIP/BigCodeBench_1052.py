
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    # Load the dataset from the CSV file
    data = pd.read_csv(file_path, header=None, names=['text'])
    
    # Initialize the CountVectorizer with the specified stop words
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    
    # Fit and transform the data
    X = vectorizer.fit_transform(data['text'])
    
    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the word counts
    word_counts = X.toarray().sum(axis=0)
    
    # Get the 10 most common words
    top_words = pd.Series(word_counts, index=feature_names).nlargest(10)
    
    # Create a histogram of the top 10 words
    fig, ax = plt.subplots()
    ax.bar(top_words.index, top_words.values)
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')
    
    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        plt.close()
        return None
    
    # Display the plot if save_path is not provided
    plt.show()
    return ax