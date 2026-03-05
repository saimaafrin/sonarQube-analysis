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
    random_numbers = [random.randint(0, RANGE) for _ in range(SIZE)]
    
    # Calculate moving average
    moving_average = []
    for i in range(SIZE):
        if i < 5:
            moving_average.append(statistics.mean(random_numbers[:i+1]))
        else:
            moving_average.append(statistics.mean(random_numbers[i-5:i+1]))
    
    # Create DataFrame
    df = pd.DataFrame({
        "Random Numbers": random_numbers,
        "Moving Average": moving_average
    })
    
    # Plot histogram
    plt.hist(random_numbers, bins=np.arange(0, RANGE+BIN_WIDTH, BIN_WIDTH), edgecolor='black')
    plt.title('Histogram of Random Numbers')
    plt.xlabel('Range')
    plt.ylabel('Frequency')
    plt.show()
    
    return df