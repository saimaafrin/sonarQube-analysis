
from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Initialize a Counter to keep track of the sums
    sum_counts = Counter()

    # Roll the dice and update the sum counts
    for _ in range(num_rolls):
        roll = sum(random.randint(1, 6) for _ in range(num_dice))
        sum_counts[roll] += 1

    # Create a bar plot of the distribution of dice roll sums
    fig, ax = plt.subplots()
    ax.bar(sum_counts.keys(), sum_counts.values(), width=1, color='b')
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')

    # Save the plot to a file if a plot_path is provided
    if plot_path:
        plt.savefig(plot_path)

    # Return the Counter and the Axes object
    return sum_counts, ax