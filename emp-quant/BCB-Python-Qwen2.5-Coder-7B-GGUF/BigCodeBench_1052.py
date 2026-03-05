
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
    
    # Check if the dataset is empty
    if df.empty:
        print("The dataset is empty.")
        return None
    
    # Extract the text data
    text_data = df['text'].dropna()
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    
    # Fit and transform the text data
    word_counts = vectorizer.fit_transform(text_data)
    
    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Get the counts of each word
    counts = word_counts.sum(axis=0).A1
    
    # Create a DataFrame to store the word counts
    word_df = pd.DataFrame({'word': feature_names, 'count': counts})
    
    # Sort the DataFrame by count in descending order
    word_df = word_df.sort_values(by='count', ascending=False)
    
    # Get the top 10 words
    top_10_words = word_df.head(10)
    
    # Plot the histogram
    fig, ax = plt.subplots()
    ax.barh(top_10_words['word'], top_10_words['count'])
    ax.set_xlabel('Count')
    ax.set_ylabel('Word')
    ax.set_title('Top 10 Most Common Words')
    
    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        return None
    
    # Display the plot
    plt.show()
    
    # Return the Axes object
    return ax