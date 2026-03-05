import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt
def task_func(url):
    # Download the text file from the specified URL
    response = urllib.request.urlopen(url)
    text = response.read().decode('utf-8')

    # Process the text to count the frequency of each word
    words = re.findall(r'\b\w+\b', text)
    word_counts = Counter(words)

    # Get the ten most common words
    most_common_words = word_counts.most_common(10)

    # Plot a bar chart showing the ten most frequently occurring words
    fig, ax = plt.subplots()
    ax.bar([word for word, count in most_common_words], [count for word, count in most_common_words])
    ax.set_xlabel('Words')
    ax.set_ylabel('Frequency')
    ax.set_title('Top 10 Most Common Words')

    return word_counts, ax