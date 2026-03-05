
import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(url):
    # Download the text file from the specified URL
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')

    # Use regular expressions to extract words from the text
    words = re.findall(r'\w+', text)

    # Create a Counter object to count word frequencies
    counter = Counter(words)

    # Sort the Counter object by word frequency
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # Extract the top 10 most common words
    top_words = sorted_counter[:10]

    # Create a bar chart of the top 10 words
    fig, ax = plt.subplots()
    ax.bar(range(1, 11), [word[1] for word in top_words])
    ax.set_xticks(range(1, 11))
    ax.set_xticklabels([word[0] for word in top_words])
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')

    return counter, ax