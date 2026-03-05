
import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(url):
    # Download the text file from the specified URL
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')

    # Use regular expression to find all words
    words = re.findall(r'\b\w+\b', text)

    # Count the frequency of each word
    word_count = Counter(words)

    # Get the ten most common words
    top_words = word_count.most_common(10)

    # Plot a bar chart of the ten most common words
    fig, ax = plt.subplots()
    ax.bar([word for word, _ in top_words], [count for _, count in top_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')

    # Return the Counter object and the Axes object
    return word_count, ax