
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
    random_numbers = [random.randint(0, RANGE) for _ in range(SIZE)]
    
    # Calculate moving average
    moving_average = []
    for i in range(len(random_numbers)):
        if i < 5:
            window = random_numbers[:i+1]
        else:
            window = random_numbers[i-5:i+1]
        moving_avg = sum(window) / len(window)
        moving_average.append(moving_avg)
    
    # Create DataFrame
    df = pd.DataFrame({
        'Random Numbers': random_numbers,
        'Moving Average': moving_average
    })
    
    # Plot histogram
    plt.figure(figsize=(10, 6))
    plt.hist(df['Random Numbers'], bins=np.arange(0, RANGE + BIN_WIDTH, BIN_WIDTH), edgecolor='black')
    plt.title('Histogram of Random Numbers')
    plt.xlabel('Range')
    plt.ylabel('Frequency')
    plt.show()
    
    return df