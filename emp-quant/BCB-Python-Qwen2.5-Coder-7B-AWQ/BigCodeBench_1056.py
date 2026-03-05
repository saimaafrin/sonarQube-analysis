import numpy as np
import random
import matplotlib.pyplot as plt
LETTERS = list("abcdefghijklmnopqrstuvwxyz")
NUMBERS = list(range(1, 27))
def task_func(n_pairs=26):
    """
    Generates and displays a bar chart representing random letter-number pairs.
    
    Parameters:
    n_pairs (int): The number of pairs to generate. Must be between 1 and 26.
    
    Returns:
    matplotlib.container.BarContainer: The bar chart object.
    
    Raises:
    ValueError: If 'n_pairs' is outside the range of 1 to 26, inclusive.
    """
    if not 1 <= n_pairs <= 26:
        raise ValueError("n_pairs must be between 1 and 26, inclusive.")
    
    # Generate random letter-number pairs
    pairs = [(LETTERS[i], NUMBERS[i]) for i in range(n_pairs)]
    random.shuffle(pairs)
    
    # Assign random counts to each pair
    counts = [random.randint(1, 9) for _ in range(n_pairs)]
    
    # Prepare data for plotting
    labels = [f"{letter}:{number}" for letter, number in pairs]
    x = np.arange(len(labels))
    width = 0.35
    
    # Create bar chart
    fig, ax = plt.subplots()
    bars = ax.bar(x, counts, width, label='Counts')
    
    # Set labels and title
    ax.set_xlabel('Letter:Number Pairs')
    ax.set_ylabel('Counts')
    ax.set_title('Random Letter:Number Pairs Chart')
    ax.set_xticks(x)
    ax.set_xticklabels(labels)
    ax.legend()
    
    # Display the plot
    plt.show()
    
    return bars