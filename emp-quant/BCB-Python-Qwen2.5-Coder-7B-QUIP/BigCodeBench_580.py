
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
    # Generate a list of random numbers
    random_numbers = [random.randint(0, RANGE) for _ in range(SIZE)]
    
    # Initialize a list to store moving averages
    moving_averages = []
    
    # Calculate the moving average for each number
    for i in range(SIZE):
        window = random_numbers[max(0, i-5):min(SIZE, i+6)]
        moving_averages.append(statistics.mean(window))
    
    # Create a DataFrame with "Random Numbers" and "Moving Average"
    df = pd.DataFrame({
        "Random Numbers": random_numbers,
        "Moving Average": moving_averages
    })
    
    # Plot a histogram of the "Random Numbers" column
    plt.hist(df["Random Numbers"], bins=np.arange(0, RANGE+1, BIN_WIDTH), edgecolor='k')
    plt.xlabel("Random Number")
    plt.ylabel("Frequency")
    plt.title("Histogram of Random Numbers")
    plt.show()
    
    return df