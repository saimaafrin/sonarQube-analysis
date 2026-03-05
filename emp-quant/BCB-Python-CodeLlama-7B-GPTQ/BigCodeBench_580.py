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
    random_numbers = [random.randint(1, RANGE) for _ in range(SIZE)]

    # Calculate moving average
    moving_average = [statistics.mean(random_numbers[i:i+5]) for i in range(SIZE-4)]

    # Create DataFrame
    df = pd.DataFrame({
        "Random Numbers": random_numbers,
        "Moving Average": moving_average
    })

    # Plot histogram
    plt.hist(df["Random Numbers"], bins=BIN_WIDTH)
    plt.show()