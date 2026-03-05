
from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize a Counter to store the sums of the dice rolls
    sum_counts = Counter()
    
    # Simulate rolling the dice multiple times
    for _ in range(num_rolls):
        roll_sum = sum(random.randint(1, 6) for _ in range(num_dice))
        sum_counts[roll_sum] += 1
    
    # Create a bar plot of the distribution of dice roll sums
    fig, ax = plt.subplots()
    ax.bar(sum_counts.keys(), sum_counts.values(), align='center')
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of Dice Roll Sums ({num_dice} dice, {num_rolls} rolls)')
    
    # Save the plot to a file if a plot_path is provided
    if plot_path:
        plt.savefig(plot_path)
    
    # Return the Counter object and the Axes object
    return sum_counts, ax