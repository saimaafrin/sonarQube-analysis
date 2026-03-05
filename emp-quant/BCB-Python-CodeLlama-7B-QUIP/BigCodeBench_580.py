
import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
# Constants
RANGE = 10000  # The range within which random numbers are generated
SIZE = 1000  # The number of random numbers to generate
BIN_WIDTH = 100  # The width of bins for the histogram

def task_func():
    # Generate random numbers
    random_numbers = np.random.randint(1, RANGE, SIZE)
    # Calculate moving average
    moving_average = np.concatenate((random_numbers, np.roll(random_numbers, 1)))
    moving_average = moving_average[1:]
    moving_average = moving_average - moving_average.mean()
    # Plot histogram
    plt.hist(random_numbers, BIN_WIDTH)
    plt.show()
    # Return DataFrame
    return pd.DataFrame({"Random Numbers": random_numbers, "Moving Average": moving_average})