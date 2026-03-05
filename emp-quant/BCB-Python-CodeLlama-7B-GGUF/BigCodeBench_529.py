
from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Initialize the counter for the dice roll sums
    counter = Counter()

    # Simulate rolling the dice num_rolls times
    for _ in range(num_rolls):
        # Roll the dice num_dice times
        roll = [random.randint(1, 6) for _ in range(num_dice)]
        # Add the sum of the roll to the counter
        counter[sum(roll)] += 1

    # Create the bar plot
    fig, ax = plt.subplots()
    ax.bar(range(1, 7), counter.values())
    ax.set_xticks(range(1, 7))
    ax.set_xticklabels(range(1, 7))
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')

    # Save the plot to a file if specified
    if plot_path:
        fig.savefig(plot_path)

    return counter, ax