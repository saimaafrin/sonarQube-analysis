
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

    # Count the frequency of each word
    word_counts = Counter(words)

    # Get the top 10 most common words
    top_words = word_counts.most_common(10)

    # Plot the bar chart
    fig, ax = plt.subplots()
    ax.bar(top_words, [word[1] for word in top_words])
    ax.set_xlabel("Word")
    ax.set_ylabel("Count")
    ax.set_title("Top 10 Most Common Words")
    plt.show()

    return top_words