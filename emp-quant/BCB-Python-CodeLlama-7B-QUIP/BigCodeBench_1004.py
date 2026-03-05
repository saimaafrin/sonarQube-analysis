
import urllib.request
import re
from collections import Counter
import matplotlib.pyplot as plt

def task_func(url):
    # Download the text file from the specified URL
    with urllib.request.urlopen(url) as response:
        text = response.read().decode('utf-8')

    # Count the frequency of each word in the text
    words = re.findall(r'\w+', text)
    counts = Counter(words)

    # Plot the bar chart of the ten most common words
    fig, ax = plt.subplots()
    ax.bar(counts.keys()[:10], counts.values())
    ax.set_xlabel('Word')
    ax.set_ylabel('Frequency')
    ax.set_title('Most Frequently Occurring Words')
    plt.show()

    return counts, ax