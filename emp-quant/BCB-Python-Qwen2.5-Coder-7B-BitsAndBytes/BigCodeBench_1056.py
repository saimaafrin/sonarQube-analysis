
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))

def task_func(n_pairs=26):
    if not 1 <= n_pairs <= 26:
        raise ValueError("n_pairs must be between 1 and 26, inclusive.")
    
    # Generate all possible letter-number pairs
    pairs = [(letter, num) for letter in LETTERS[:n_pairs] for num in NUMBERS]
    
    # Shuffle the pairs
    random.shuffle(pairs)
    
    # Assign random counts to each pair
    counts = [random.randint(1, 9) for _ in range(len(pairs))]
    
    # Extract labels and values for plotting
    labels = [f"{pair[0]}:{pair[1]}" for pair in pairs]
    values = counts
    
    # Create the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(labels, values)
    
    # Set the title and axis labels
    ax.set_title("Random Letter:Number Pairs Chart")
    ax.set_xlabel("Letter:Number Pairs")
    ax.set_ylabel("Counts")
    
    # Display the plot
    plt.show()
    
    return bars