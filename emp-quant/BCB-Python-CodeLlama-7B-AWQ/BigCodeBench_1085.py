import re
from collections import Counter
import matplotlib.pyplot as plt
def task_func(text):
    """
    Analyzes the frequency of words in a given text after lowercasing, removing punctuation, splitting into words, and plots the top 10 most common words.
    The function should output with:
        list: A list of tuples containing the 10 most common words and their counts.
        Axes: The matplotlib Axes object of the bar chart.
    """
    # Lowercase the text
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into individual words
    words = text.split()

    # Create a Counter object to keep track of word frequencies
    word_counts = Counter(words)

    # Sort the Counter object by word frequency and get the top 10 most common words
    top_words = word_counts.most_common(10)

    # Create a bar chart of the top 10 most common words
    fig, ax = plt.subplots()
    ax.bar(range(1, 11), [word_count for word, word_count in top_words])
    ax.set_xticks(range(1, 11))
    ax.set_xticklabels([word for word, word_count in top_words])
    ax.set_ylabel('Word frequency')
    ax.set_title('Top 10 most common words')

    return top_words, ax
text = "This is a sample text with some words repeated. This is a sample text with some words repeated."