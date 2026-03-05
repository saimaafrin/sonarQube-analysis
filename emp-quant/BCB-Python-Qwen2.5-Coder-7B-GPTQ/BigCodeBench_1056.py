import numpy as np
import random
import matplotlib.pyplot as plt
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))
def task_func(n_pairs=26):
    """
    Generates and displays a bar chart representing random letter-number pairs.
    
    Parameters:
    n_pairs (int): The number of pairs to generate. Must be between 1 and 26, inclusive.
    
    Returns:
    matplotlib.container.BarContainer: The bar chart created by the function.
    
    Raises:
    ValueError: If 'n_pairs' is outside the range of 1 to 26, inclusive.
    """
    if not 1 <= n_pairs <= 26:
        raise ValueError("n_pairs must be between 1 and 26, inclusive.")
    
    # Generate letter-number pairs
    pairs = [f"{LETTERS[i]}:{NUMBERS[i]}" for i in range(n_pairs)]
    
    # Shuffle the pairs
    random.shuffle(pairs)
    
    # Assign random counts to each pair
    counts = [random.randint(1, 9) for _ in range(n_pairs)]
    
    # Create the bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(pairs, counts, color='blue')
    
    # Set the title and labels
    ax.set_title("Random Letter:Number Pairs Chart")
    ax.set_xlabel("Letter:Number Pairs")
    ax.set_ylabel("Counts")
    
    # Show the plot
    plt.show()
    
    return bars