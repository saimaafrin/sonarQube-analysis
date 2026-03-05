from collections import Counter
import random
import matplotlib.pyplot as plt
def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    """
    Simulate rolling a certain number of a standard six-sided dice several times, then identify and display the distribution of the sums of the dice rolls in a bar plot.
    """
    # Set the random seed for reproducibility
    random.seed(random_seed)

    # Initialize the counter for the distribution of dice roll sums
    counter = Counter()

    # Simulate rolling the dice
    for i in range(num_rolls):
        # Roll the dice
        roll = sum(random.randint(1, 6) for _ in range(num_dice))

        # Increment the counter for the current roll sum
        counter[roll] += 1

    # Create the bar plot
    fig, ax = plt.subplots()
    ax.bar(range(1, 7), counter.values())
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')

    # Save the plot to a file if specified
    if plot_path:
        fig.savefig(plot_path)

    # Return the counter and the bar plot
    return counter, ax