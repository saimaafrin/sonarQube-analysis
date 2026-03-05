from collections import Counter
import random
import matplotlib.pyplot as plt
def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    # Set the random seed for reproducibility
    random.seed(random_seed)
    
    # Initialize a list to store the sums of dice rolls
    sums = []
    
    # Roll the dice and calculate the sum for each roll
    for _ in range(num_rolls):
        roll_sum = sum(random.randint(1, 6) for _ in range(num_dice))
        sums.append(roll_sum)
    
    # Count the occurrences of each sum
    sum_counts = Counter(sums)
    
    # Create a bar plot of the distribution of dice roll sums
    fig, ax = plt.subplots()
    ax.bar(sum_counts.keys(), sum_counts.values(), tick_label=sum_counts.keys())
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title('Distribution of Dice Roll Sums')
    
    # Save the plot to the specified path if provided
    if plot_path:
        plt.savefig(plot_path)
    
    # Show the plot
    plt.show()
    
    # Return the Counter object and the Axes object
    return sum_counts, ax