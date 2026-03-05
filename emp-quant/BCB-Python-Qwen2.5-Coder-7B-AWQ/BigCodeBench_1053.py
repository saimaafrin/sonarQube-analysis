import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
import matplotlib.pyplot as plt
STOP_WORDS = ["a", "an", "the", "in", "on", "at", "and", "or"]
def task_func(file_path, save_path=None):
    try:
        # Read the CSV file
        data = pd.read_csv(file_path)
        # Check if the column 'Text' exists
        if 'Text' not in data.columns:
            raise ValueError("The CSV file must contain a column named 'Text'.")
        # Initialize CountVectorizer with stopwords
        vectorizer = CountVectorizer(stop_words=STOP_WORDS)
        # Fit and transform the text data
        X = vectorizer.fit_transform(data['Text'])
        # Get feature names and their counts
        feature_names = vectorizer.get_feature_names_out()
        counts = X.toarray().sum(axis=0)
        # Create a dictionary of word counts
        word_counts = dict(zip(feature_names, counts))
        # Sort the dictionary by count in descending order
        sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)
        # Get the top 10 most common words
        top_10_words = sorted_word_counts[:10]
        # Create a bar plot
        fig, ax = plt.subplots()
        ax.bar([word for word, count in top_10_words], [count for word, count in top_10_words])
        ax.set_xlabel('Words')
        ax.set_ylabel('Frequency')
        ax.set_title('Top 10 Most Common Words')
        # Save the plot if save_path is provided
        if save_path:
            plt.savefig(save_path)
            plt.close()
            return None
        else:
            return ax
    except FileNotFoundError:
        raise FileNotFoundError(f"The file at {file_path} was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")
        return None