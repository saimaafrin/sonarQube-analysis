import numpy as np
import random
import matplotlib.pyplot as plt
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))
def task_func(n_pairs=26):
    """
    Generates and displays a bar chart representing random letter-number pairs.
    Each bar corresponds to a unique pair, formed by combining a letter from 'a' to 'z' with a number from 1 to 26.
    The function randomly shuffles these pairs and assigns a random count to each.
    """
    if n_pairs < 1 or n_pairs > 26:
        raise ValueError("n_pairs must be between 1 and 26, inclusive")

    # Generate random pairs
    pairs = [(random.choice(LETTERS), random.choice(NUMBERS)) for _ in range(n_pairs)]

    # Shuffle the pairs
    random.shuffle(pairs)

    # Assign random counts to each pair
    counts = [random.randint(1, 9) for _ in range(n_pairs)]

    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(pairs, counts)
    ax.set_title("Random Letter:Number Pairs Chart")
    ax.set_xlabel("Letter:Number Pairs")
    ax.set_ylabel("Counts")
    plt.show()