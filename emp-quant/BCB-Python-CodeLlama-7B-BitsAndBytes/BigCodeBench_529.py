
from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Initialize a counter to keep track of the counts of each sum
    counter = Counter()

    # Roll the dice num_rolls times and update the counter
    for _ in range(num_rolls):
        roll = sum(random.randint(1, num_dice) for _ in range(num_dice))
        counter[roll] += 1

    # Create a bar plot of the distribution of dice roll sums
    fig, ax = plt.subplots()
    ax.bar(range(1, num_dice + 1), counter.values())
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')

    # Save the plot to a file if a path is provided
    if plot_path:
        fig.savefig(plot_path)

    return counter, ax