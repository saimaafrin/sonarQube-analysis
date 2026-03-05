import numpy as np
import matplotlib.pyplot as plt
import random
NUMBERS = list(range(1, 7))
def task_func(rolls, seed=None):
    if seed is not None:
        random.seed(seed)
    
    # Simulate dice rolls
    results = [random.choice(NUMBERS) for _ in range(rolls)]
    
    # Calculate frequency of each result
    frequency = np.zeros(6)
    for result in results:
        frequency[result - 1] += 1
    
    # Create histogram
    fig, ax = plt.subplots()
    ax.bar(NUMBERS, frequency, tick_label=NUMBERS)
    ax.set_title("Histogram of Dice Rolls")
    ax.set_xlabel("Dice Value")
    ax.set_ylabel("Frequency")
    
    return frequency, ax