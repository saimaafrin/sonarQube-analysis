
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
    random_numbers = random.sample(range(RANGE), SIZE)

    # Calculate moving average
    moving_average = statistics.moving_average(random_numbers, 5)

    # Create DataFrame
    df = pd.DataFrame({
        "Random Numbers": random_numbers,
        "Moving Average": moving_average
    })

    # Plot histogram
    plt.hist(df["Random Numbers"], bins=BIN_WIDTH)
    plt.show()

    return df

task_func()