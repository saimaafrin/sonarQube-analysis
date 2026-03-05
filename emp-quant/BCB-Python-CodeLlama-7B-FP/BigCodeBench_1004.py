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

    # Create a Counter object to count word frequencies
    counter = Counter(words)

    # Sort the Counter object by word frequency
    sorted_counter = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # Extract the top ten most common words
    top_ten = sorted_counter[:10]

    # Create a bar chart of the top ten most common words
    fig, ax = plt.subplots()
    ax.bar(range(1, 11), [word[1] for word in top_ten])
    ax.set_xticks(range(1, 11))
    ax.set_xticklabels([word[0] for word in top_ten])
    ax.set_ylabel('Frequency')
    ax.set_title('Top Ten Most Common Words')

    return counter, ax
url = 'https://raw.githubusercontent.com/text-files/lorem-ipsum/master/lorem-ipsum.txt'