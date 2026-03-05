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
    for i in range(len(random_numbers)):
        window = random_numbers[max(0, i-5):i+1]
        moving_average.append(statistics.mean(window))
    
    # Create DataFrame
    df = pd.DataFrame({
        "Random Numbers": random_numbers,
        "Moving Average": moving_average
    })
    
    # Plot histogram
    plt.hist(random_numbers, bins=np.arange(0, RANGE + BIN_WIDTH, BIN_WIDTH))
    plt.title('Histogram of Random Numbers')
    plt.xlabel('Random Numbers')
    plt.ylabel('Frequency')
    plt.show()
    
    return df