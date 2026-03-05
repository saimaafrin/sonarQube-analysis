
from collections import Counter
import random
import matplotlib.pyplot as plt

def task_func(num_rolls, num_dice, plot_path=None, random_seed=0):
    random.seed(random_seed)
    dice_sums = [sum(random.randint(1, 6) for _ in range(num_dice)) for _ in range(num_rolls)]
    sum_counter = Counter(dice_sums)
    
    fig, ax = plt.subplots()
    ax.bar(sum_counter.keys(), sum_counter.values(), color='blue')
    ax.set_xlabel('Sum of Dice Roll')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of Dice Roll Sums for {num_dice} dice')
    
    if plot_path:
        plt.savefig(plot_path)
    
    plt.show()
    
    return sum_counter, ax