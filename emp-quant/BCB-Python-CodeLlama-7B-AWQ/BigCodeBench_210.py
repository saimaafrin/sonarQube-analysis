import collections
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Generate a bar plot showing the frequency of letters in the given dataset, and highlight the letter associated with the maximum integer value.
    """
    # Create a dictionary to store the letter counts
    letter_counts = collections.Counter(data)

    # Get the maximum value and its corresponding letter
    max_value = max(letter_counts.values())
    max_letter = max(letter_counts, key=itemgetter(1))

    # Create the bar plot
    fig, ax = plt.subplots()
    ax.bar(letter_counts.keys(), letter_counts.values())
    ax.set_xlabel('Letter')
    ax.set_ylabel('Count')
    ax.set_title('Letter Counts with Max Value Letter Highlighted')
    ax.legend(['Letter Counts', 'Max Value Letter'])

    # Highlight the maximum value letter
    ax.text(max_letter, max_value, max_letter, ha='center', va='bottom')

    return ax
data = ['a', 'b', 'c', 'a', 'b', 'c', 'a', 'b', 'c']