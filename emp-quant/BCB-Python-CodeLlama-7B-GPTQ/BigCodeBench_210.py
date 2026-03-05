import collections
from operator import itemgetter
import matplotlib.pyplot as plt
def task_func(data):
    """
    Generate a bar plot showing the frequency of letters in the given dataset, and highlight the letter associated with the maximum integer value.
    The function should output with:
        matplotlib.axes.Axes: The Axes object of the generated plot, with the x-axis labeled 'Letter', the y-axis labeled 'Count', the title 'Letter Counts with Max Value Letter Highlighted', and the labels 'Letter Counts' and 'Max Value Letter' in the legend.
    """
    # Create a dictionary to store the letter counts
    letter_counts = collections.Counter(data)

    # Sort the dictionary by value in descending order
    sorted_letter_counts = sorted(letter_counts.items(), key=itemgetter(1), reverse=True)

    # Get the maximum value and its corresponding letter
    max_value = sorted_letter_counts[0][1]
    max_letter = sorted_letter_counts[0][0]

    # Create a bar plot with the letter counts
    fig, ax = plt.subplots()
    ax.bar(letter_counts.keys(), letter_counts.values())
    ax.set_xlabel('Letter')
    ax.set_ylabel('Count')
    ax.set_title('Letter Counts with Max Value Letter Highlighted')
    ax.legend(['Letter Counts', 'Max Value Letter'])

    # Highlight the maximum value letter
    ax.text(max_letter, max_value, max_letter, ha='center', va='bottom', fontsize=12)

    return ax
data = 'abcdefghijklmnopqrstuvwxyz'