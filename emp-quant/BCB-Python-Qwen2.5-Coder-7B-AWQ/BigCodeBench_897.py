import numpy as np
import matplotlib.pyplot as plt
import random
NUMBERS = list(range(1, 7))
def task_func(rolls, seed=None):
    """
    Simulate a number of dice rolls, calculate the frequency of each result,
    and return both the frequency array and a histogram of the results.

    Parameters:
    rolls (int): The number of dice rolls to simulate.
    seed (int, optional): The seed for the random number generator.

    Returns:
    tuple: A tuple containing:
        np.array: A numpy array with the frequency of each outcome.
        matplotlib.Axes: Axes object representing the histogram.
    """
    if seed is not None:
        random.seed(seed)

    # Simulate dice rolls
    results = [random.choice(NUMBERS) for _ in range(rolls)]

    # Calculate frequency of each outcome
    frequency = np.zeros(len(NUMBERS))
    for result in results:
        frequency[result - 1] += 1

    # Create histogram
    fig, ax = plt.subplots()
    ax.bar(NUMBERS, frequency, tick_label=NUMBERS)
    ax.set_title("Histogram of Dice Rolls")
    ax.set_xlabel("Dice Value")
    ax.set_ylabel("Frequency")

    return frequency, ax