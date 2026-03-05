
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))

def task_func(n_pairs=26):
    if not (1 <= n_pairs <= 26):
        raise ValueError("n_pairs must be between 1 and 26, inclusive.")
    
    # Generate all possible letter-number pairs
    pairs = [f"{letter}:{number}" for letter in LETTERS for number in NUMBERS]
    
    # Shuffle the pairs
    random.shuffle(pairs)
    
    # Select the first n_pairs
    selected_pairs = pairs[:n_pairs]
    
    # Assign random counts to each pair
    counts = [random.randint(1, 9) for _ in range(n_pairs)]
    
    # Prepare data for plotting
    labels = selected_pairs
    values = counts
    
    # Create the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values)
    
    # Set the title and labels
    ax.set_title("Random Letter:Number Pairs Chart")
    ax.set_xlabel("Letter:Number Pairs")
    ax.set_ylabel("Counts")
    
    # Display the chart
    plt.show()
    
    return bars