
import time
import random
import matplotlib.pyplot as plt
from scipy.stats import kurtosis

def task_func(intervals=100, seed=0):
    # Set the seed for the random number generator
    random.seed(seed)
    
    # Initialize the list to store the random numbers
    random_numbers = []
    
    # Initialize the list to store the elapsed times
    elapsed_times = []
    
    # Start the timer
    start_time = time.time()
    
    # Generate the random numbers
    for _ in range(intervals):
        # Generate a random number
        random_number = random.random()
        
        # Append the random number to the list
        random_numbers.append(random_number)
        
        # Append the elapsed time to the list
        elapsed_times.append(time.time() - start_time)
        
        # Wait for 1 second
        time.sleep(1)
    
    # Plot the random numbers as a function of elapsed time
    fig, ax = plt.subplots()
    ax.plot(elapsed_times, random_numbers)
    
    # Calculate the kurtosis of the random numbers
    kurt = kurtosis(random_numbers)
    
    # Return the Axes object and the kurtosis value
    return ax, kurt