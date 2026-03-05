import re
from collections import Counter
import matplotlib.pyplot as plt
def task_func(text):
    # Lowercase the text
    text = text.lower()

    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)

    # Split the text into words
    words = text.split()

    # Create a Counter object to count the words
    counter = Counter(words)

    # Get the top 10 most common words
    top_words = counter.most_common(10)

    # Create a bar chart of the top 10 words
    fig, ax = plt.subplots()
    ax.bar(top_words.keys(), top_words.values())
    ax.set_xlabel('Word')
    ax.set_ylabel('Count')
    ax.set_title('Top 10 Most Common Words')

    # Return the list of tuples and the Axes object
    return top_words, ax
text = 'This is a sample text with some words repeated.'