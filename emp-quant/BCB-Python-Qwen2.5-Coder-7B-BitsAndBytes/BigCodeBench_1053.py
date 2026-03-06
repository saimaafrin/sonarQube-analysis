
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt

# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check if the DataFrame has the required column
        if 'Text' not in df.columns:
            raise ValueError("CSV file must contain a column named 'Text'")
        
        # Concatenate all text data into a single string
        text_data = ' '.join(df['Text'].dropna())
        
        # Initialize CountVectorizer with English stop words
        vectorizer = CountVectorizer(stop_words='english', lowercase=True)
        
        # Fit and transform the text data
        X = vectorizer.fit_transform([text_data])
        
        # Get feature names (words) and their counts
        feature_names = vectorizer.get_feature_names_out()
        counts = X.toarray()[0]
        
        # Create a dictionary of word counts
        word_counts = dict(zip(feature_names, counts))
        
        # Sort the words by count in descending order
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        
        # Take the top 10 most common words
        top_10_words, top_10_counts = zip(*sorted_word_counts[:10])
        
        # Plotting
        fig, ax = plt.subplots()
        ax.barh(top_10_words, top_10_counts, color='skyblue')
        ax.set_xlabel('Frequency')
        ax.set_title('Top 10 Most Common Words')
        
        if save_path:
            plt.savefig(save_path)
            return None
        else:
            return ax
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None