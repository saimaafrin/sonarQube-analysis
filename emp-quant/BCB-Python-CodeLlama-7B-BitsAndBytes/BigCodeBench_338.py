
import random
import string
from matplotlib import pyplot as plt

def task_func(elements, seed=100):
    # Set the random seed for reproducibility
    random.seed(seed)

    # Create a list of random alphanumeric strings of length 5
    random_strings = [random.choice(string.ascii_letters + string.digits) for _ in range(5)]

    # Format each string in the list with the pattern "% {0}%"
    formatted_strings = ["% " + random_string + "%" for random_string in random_strings]

    # Create a histogram of the occurrence of each character across all the strings
    char_counts = {}
    for formatted_string in formatted_strings:
        for char in formatted_string:
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1

    # Create the histogram plot
    fig, ax = plt.subplots()
    ax.bar(char_counts.keys(), char_counts.values())
    ax.set_xlabel("Character")
    ax.set_ylabel("Count")
    ax.set_title("Histogram of Character Occurrence in Formatted Strings")

    return formatted_strings, ax, char_counts