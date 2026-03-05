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
    for _ in range(num_rolls):
        # Roll the dice
        roll = random.randint(1, num_dice)

        # Add the roll to the counter
        counter[roll] += 1

    # Create the bar plot
    fig, ax = plt.subplots()
    ax.bar(range(num_dice + 1), counter.values())
    ax.set_xlabel("Sum of Dice Roll")
    ax.set_ylabel("Count")
    ax.set_title("Distribution of Dice Roll Sums")

    # Save the plot to a file if specified
    if plot_path:
        fig.savefig(plot_path)

    # Return the counter and the plot
    return counter, ax