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

    # Use a regular expression to identify words in the text
    words = re.findall(r'\w+', text)

    # Create a Counter object to count the frequency of each word
    counter = Counter(words)

    # Sort the Counter object by word frequency and take the top ten words
    top_ten = counter.most_common(10)

    # Create a bar chart of the top ten words
    fig, ax = plt.subplots()
    ax.bar(range(10), [word[1] for word in top_ten])
    ax.set_xticks(range(10))
    ax.set_xticklabels([word[0] for word in top_ten])
    ax.set_ylabel('Frequency')
    ax.set_title('Top Ten Most Frequent Words')

    return counter, ax
url = 'https://raw.githubusercontent.com/text-files/hello-world.txt'