
import numpy as np
import random
import matplotlib.pyplot as plt

# Constants
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))

def task_func(n_pairs=26):
    if n_pairs < 1 or n_pairs > 26:
        raise ValueError("n_pairs must be between 1 and 26, inclusive.")
    
    # Generate all possible letter-number pairs
    pairs = [f"{LETTERS[i]}:{NUMBERS[j]}" for i in range(n_pairs) for j in range(n_pairs)]
    
    # Shuffle the pairs
    random.shuffle(pairs)
    
    # Assign random counts to each pair
    counts = [random.randint(1, 9) for _ in range(n_pairs)]
    
    # Create a bar chart
    fig, ax = plt.subplots()
    ax.bar(pairs, counts, color='blue')
    
    # Set the title and labels
    ax.set_title("Random Letter:Number Pairs Chart")
    ax.set_xlabel("Letter:Number Pairs")
    ax.set_ylabel("Counts")
    
    # Display the chart
    plt.show()
    
    return ax