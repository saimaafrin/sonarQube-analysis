
import numpy as np
import random
import matplotlib.pyplot as plt
# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))
def task_func(n_pairs=26):
    if n_pairs < 1 or n_pairs > 26:
        raise ValueError("n_pairs must be between 1 and 26")
    pairs = [(letter, number) for letter in LETTERS for number in NUMBERS]
    random.shuffle(pairs)
    counts = [random.randint(1, 9) for _ in range(n_pairs)]
    bar_labels = [f"{letter}:{number}" for letter, number in pairs]
    bar_chart = plt.bar(bar_labels, counts, title="Random Letter:Number Pairs Chart", xlabel="Letter:Number Pairs", ylabel="Counts")
    return bar_chart