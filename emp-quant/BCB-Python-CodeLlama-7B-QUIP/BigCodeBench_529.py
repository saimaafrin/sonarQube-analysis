
from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Initialize the Counter object to count the number of times each sum appears
    counter = Counter()

    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Roll the dice a specified number of times
    for i in range(num_rolls):
        # Roll the dice
        rolls = [random.randint(1, num_dice) for i in range(num_dice)]
        # Add the sum of the rolls to the counter
        counter.update([sum(rolls)])

    # Create a bar plot of the distribution of dice roll sums
    fig, ax = plt.subplots()
    ax.bar(counter.keys(), counter.values(), width=1, color='blue')
    ax.set_xlabel('Sum of Dice Rolls')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')
    if plot_path:
        fig.savefig(plot_path)
    return counter, fig, ax