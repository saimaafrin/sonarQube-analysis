
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
# Constants
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]

def task_func(file_path, save_path=None):
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)
        
        # Check if the file has a header
        if 'Text' not in df.columns:
            df.columns = ['Text']
        
        # Concatenate all text data into a single string
        text_data = ' '.join(df['Text'])
        
        # Initialize CountVectorizer with stopwords
        vectorizer = CountVectorizer(stop_words=STOP_WORDS)
        
        # Fit and transform the text data
        X = vectorizer.fit_transform([text_data])
        
        # Get the feature names and their counts
        feature_names = vectorizer.get_feature_names_out()
        counts = X.toarray()[0]
        
        # Create a dictionary of word counts
        word_counts = dict(zip(feature_names, counts))
        
        # Sort the words by frequency and get the top 10
        top_10_words = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)[:10]
        
        # Prepare data for plotting
        words, counts = zip(*top_10_words)
        
        # Create a bar plot
        fig, ax = plt.subplots()
        ax.bar(words, counts, color='blue')
        ax.set_xlabel('Words')
        ax.set_ylabel('Frequency')
        ax.set_title('Top 10 Most Common Words')
        ax.set_xticklabels(words, rotation=45)
        
        # Save the plot if save_path is provided
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