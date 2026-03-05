from collections import Counter
import random
import matplotlib.pyplot as plt
def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize a Counter to store the sums of dice rolls
    sum_counter = Counter()
    
    # Roll the dice and calculate the sums
    for _ in range(num_rolls):
        roll_sum = sum(random.randint(1, 6) for _ in range(num_dice))
        sum_counter[roll_sum] += 1
    
    # Create a bar plot of the distribution of dice roll sums
    fig, ax = plt.subplots()
    ax.bar(sum_counter.keys(), sum_counter.values(), align='center')
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {num_dice} Dice Roll Sums')
    
    # Save the plot to the specified path if provided
    if plot_path:
        plt.savefig(plot_path)
    
    # Return the Counter object and the Axes object
    return sum_counter, ax