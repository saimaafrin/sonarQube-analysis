
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
        print(f"File not found: {file_path}")
        return None
    except pd.errors.EmptyDataError:
        print("The file is empty.")
        return None
    except pd.errors.ParserError:
        print(f"Error parsing the file: {file_path}")
        return None

    # Check if the 'text' column exists
    if 'text' not in df.columns:
        print("The CSV file does not contain a 'text' column.")
        return None

    # Vectorize the text data
    vectorizer = CountVectorizer(stop_words=STOP_WORDS)
    X = vectorizer.fit_transform(df['text'])
    feature_names = vectorizer.get_feature_names_out()

    # Get the counts of each word
    word_counts = X.sum(axis=0).A1
    word_counts_dict = dict(zip(feature_names, word_counts))

    # Sort the words by count in descending order
    sorted_word_counts = sorted(word_counts_dict.items(), key=lambda x: x[1], reverse=True)

    # Get the top 10 most common words
    top_10_words = sorted_word_counts[:10]

    # Create a histogram of the top 10 words
    fig, ax = plt.subplots()
    ax.bar([word[0] for word in top_10_words], [word[1] for word in top_10_words])
    ax.set_title('Top 10 Most Common Words')
    ax.set_xlabel('Words')
    ax.set_ylabel('Counts')

    # Save the plot if save_path is provided
    if save_path:
        plt.savefig(save_path)
        return None

    # Display the plot if save_path is not provided
    plt.show()
    return ax