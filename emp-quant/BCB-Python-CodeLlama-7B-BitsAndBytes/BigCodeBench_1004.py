
import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(url):
    # Download the text file from the URL
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')

    # Create a regular expression to identify words
    pattern = re.compile(r'\w+')

    # Use the regular expression to extract words from the text
    words = pattern.findall(text)

    # Create a Counter object to count the frequencies of each word
    counter = Counter(words)

    # Get the top 10 most common words
    top_words = counter.most_common(10)

    # Create a bar chart of the top 10 words
    fig, ax = plt.subplots()
    ax.bar(range(10), [w[1] for w in top_words])
    ax.set_xticks(range(10))
    ax.set_xticklabels([w[0] for w in top_words])
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Words')

    return counter, ax