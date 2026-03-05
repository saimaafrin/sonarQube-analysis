
import unicodedata
import csv
from collections import Counter
import matplotlib.pyplot as plt

def task_func(csv_file):
    """
    Reads a CSV file, normalizes the text in it to ASCII, counts the words, and returns the 10 most common words along with their frequencies as a matplotlib bar plot and a list of tuples.
    """
    try:
        with open(csv_file, 'r') as f:
            reader = csv.reader(f)
            text = [row[0] for row in reader]
    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file {csv_file} not found")
    except IOError:
        raise IOError(f"Error reading CSV file {csv_file}")

    # Normalize text to ASCII
    text = [unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode('ascii') for t in text]

    # Count words
    counter = Counter(text)

    # Get 10 most common words
    most_common = counter.most_common(10)

    # Create bar plot
    fig, ax = plt.subplots()
    ax.bar(range(10), [freq for word, freq in most_common])
    ax.set_xticks(range(10))
    ax.set_xticklabels([word for word, freq in most_common])
    ax.set_ylabel('Frequency')
    ax.set_title('10 Most Common Words')

    return (ax, most_common)