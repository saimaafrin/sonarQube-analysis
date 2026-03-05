
import unicodedata
import csv
from collections import Counter
import matplotlib.pyplot as plt

def task_func(csv_file):
    # Open the CSV file and read it line by line
    with open(csv_file, "r") as f:
        lines = f.readlines()

    # Normalize the text to ASCII
    normalized_text = [line.strip() for line in lines]

    # Count the words in the text
    word_counts = Counter(normalized_text)

    # Get the 10 most common words and their frequencies
    top_words = word_counts.most_common(10)

    # Create a bar plot of the 10 most common words
    fig, ax = plt.subplots()
    ax.bar(range(10), [word for word, _ in top_words])
    ax.set_ylabel("Frequency")
    ax.set_xlabel("Word")
    ax.set_xticklabels(range(10))
    ax.set_yticklabels(["{:.2f}".format(freq) for _, freq in top_words])
    ax.set_title("Top 10 Words in the Text")
    plt.show()

    return top_words