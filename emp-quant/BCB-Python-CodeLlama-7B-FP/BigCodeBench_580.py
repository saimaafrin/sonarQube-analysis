import pandas as pd
import random
import statistics
import matplotlib.pyplot as plt
import numpy as np
RANGE = 10000
SIZE = 1000
BIN_WIDTH = 100
def task_func():
    # Generate random numbers
    random_numbers = random.sample(range(RANGE), SIZE)

    # Calculate moving average
    moving_average = statistics.mean(random_numbers)

    # Create DataFrame
    df = pd.DataFrame({
        "Random Numbers": random_numbers,
        "Moving Average": [moving_average] * SIZE
    })

    # Plot histogram
    plt.hist(df["Random Numbers"], bins=BIN_WIDTH)
    plt.show()

    return df