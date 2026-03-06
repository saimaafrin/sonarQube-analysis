
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))

def task_func(n_pairs=26):
    if n_pairs < 1 or n_pairs > 26:
        raise ValueError("n_pairs must be between 1 and 26, inclusive")

    # Generate random letter-number pairs
    pairs = [(random.choice(LETTERS), random.choice(NUMBERS)) for _ in range(n_pairs)]

    # Shuffle the pairs and assign random counts to each
    random.shuffle(pairs)
    counts = [random.randint(1, 9) for _ in range(n_pairs)]

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(range(n_pairs), counts, label="Counts")
    ax.set_xlabel("Letter:Number Pairs")
    ax.set_ylabel("Counts")
    ax.set_title("Random Letter:Number Pairs Chart")
    ax.legend()

    # Label the bars with the corresponding letter-number pairs
    for i, (letter, number) in enumerate(pairs):
        ax.text(i, counts[i], f"{letter}:{number}", ha="center", va="center")

    return fig

# Call the function and display the chart
fig = task_func(n_pairs=10)
plt.show()