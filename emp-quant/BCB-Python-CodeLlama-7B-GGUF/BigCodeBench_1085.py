
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

    # Create a Counter object
    counter = Counter(words)

    # Get the top 10 most common words
    top_words = counter.most_common(10)

    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(range(10), [word[1] for word in top_words])
    ax.set_xticks(range(10))
    ax.set_xticklabels([word[0] for word in top_words])
    ax.set_ylabel('Count')
    ax.set_title('Top 10 Most Common Words')

    return top_words, ax

# Show the bar chart
plt.show()