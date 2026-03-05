
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check if the file has a header and use the correct column
        if 'Text' in df.columns:
            text_data = df['Text']
        else:
            text_data = df.iloc[:, 0]
        
        # Initialize CountVectorizer with stopwords
        vectorizer = CountVectorizer(stop_words=STOP_WORDS)
        
        # Fit and transform the text data
        X = vectorizer.fit_transform(text_data)
        
        # Get the feature names (words)
        feature_names = vectorizer.get_feature_names_out()
        
        # Get the counts of each word
        counts = X.toarray().sum(axis=0)
        
        # Create a DataFrame with words and their counts
        word_counts = pd.DataFrame({'Word': feature_names, 'Count': counts})
        
        # Sort the DataFrame by count in descending order and get the top 10 words
        top_10_words = word_counts.sort_values(by='Count', ascending=False).head(10)
        
        # Plot the histogram
        fig, ax = plt.subplots()
        ax.barh(top_10_words['Word'], top_10_words['Count'])
        ax.set_xlabel('Count')
        ax.set_ylabel('Word')
        ax.set_title('Top 10 Most Common Words')
        
        # Save the plot if save_path is provided
        if save_path:
            plt.savefig(save_path)
            return None
        else:
            return ax
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None