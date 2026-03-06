
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
    # Generate a list of random integers
    random_numbers = [random.randint(1, RANGE) for _ in range(SIZE)]

    # Calculate the moving average of the random integers
    moving_average = statistics.moving_average(random_numbers, 5)

    # Create a DataFrame with the random numbers and the moving average
    df = pd.DataFrame({'Random Numbers': random_numbers, 'Moving Average': moving_average})

    # Plot a histogram of the random numbers
    plt.hist(df['Random Numbers'], bins=BIN_WIDTH)
    plt.show()

    return df

# Call the function
task_func()