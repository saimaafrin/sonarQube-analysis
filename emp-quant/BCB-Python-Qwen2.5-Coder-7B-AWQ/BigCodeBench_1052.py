import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]
def task_func(file_path, save_path=None):
    # Load the dataset
    try:
        data = pd.read_csv(file_path)
    except FileNotFoundError:
        print("File not found.")
        return None
    if 'text' not in data.columns:
        print("CSV file does not contain a 'text' column.")
        return None
    
    # Initialize the vectorizer
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    
    # Fit and transform the text data
    X = vectorizer.fit_transform(data['text'])
    
    # Get the feature names
    feature_names = vectorizer.get_feature_names_out()
    
    # Sum the counts for each word
    word_counts = X.sum(axis=0)
    
    # Create a dictionary of word counts
    word_dict = dict(zip(feature_names, word_counts))
    
    # Sort the dictionary by word count in descending order
    sorted_word_dict = dict(sorted(word_dict.items(), key=lambda item: item[1], reverse=True))
    
    # Get the top 10 words
    top_10_words = list(sorted_word_dict.keys())[:10]
    top_10_counts = list(sorted_word_dict.values())[:10]
    
    # Create a histogram of the top 10 words
    plt.figure(figsize=(10, 5))
    plt.barh(top_10_words, top_10_counts, color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title('Top 10 Most Common Words')
    
    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        plt.close()
        return None
    
    # Display the plot and return the Axes object
    plt.show()
    return plt.gca()