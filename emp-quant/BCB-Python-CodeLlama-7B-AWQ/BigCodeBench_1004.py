import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt
def task_func(url):
    """
    Downloads a text file from a specified URL, processes the text to count the frequency of each word, and then plots a bar chart showing the ten most frequently occurring words.
    """
    # Download the text file from the specified URL
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')

    # Identify words using a basic regular expression
    words = re.findall(r'\w+', text)

    # Count the frequency of each word
    word_counts = Counter(words)

    # Create a bar chart of the ten most common words
    ax = plt.subplot(111)
    ax.bar(range(10), word_counts.most_common(10))
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    ax.set_title('Most Common Words')

    return word_counts, ax
url = 'https://raw.githubusercontent.com/text-files/text-files-for-tests/master/text-files/lorem-ipsum.txt'