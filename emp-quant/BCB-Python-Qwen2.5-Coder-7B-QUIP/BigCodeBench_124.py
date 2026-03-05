
from random import randint, seed as random_seed
import time
import matplotlib.pyplot as plt

def task_func(my_list, size=100, seed=100):
    # Check if my_list is a list
    if not isinstance(my_list, list):
        raise TypeError("Input 'my_list' must be a list.")
    
    # Check if all elements in my_list are numeric (int or float)
    if not all(isinstance(x, (int, float)) for x in my_list):
        raise ValueError("All elements in 'my_list' must be numeric (int or float).")
    
    # Append 12 to my_list
    my_list.append(12)
    
    # Calculate the sum of elements in my_list
    total_sum = sum(my_list)
    
    # Ensure the total_sum does not exceed the size
    if total_sum > size:
        raise ValueError("The sum of 'my_list' exceeds the specified 'size'.")
    
    # Initialize the random seed
    random_seed(seed)
    
    # Generate a list of random integers
    random_numbers = [randint(1, 100) for _ in range(total_sum)]
    
    # Measure the time taken to generate the list
    start_time = time.time()
    random_numbers = [randint(1, 100) for _ in range(total_sum)]
    end_time = time.time()
    time_taken = end_time - start_time
    
    # Plot a histogram of the generated random numbers
    plt.figure()
    plt.hist(random_numbers, bins=range(1, 101), edgecolor='k')
    plt.xlabel('Number')
    plt.ylabel('Frequency')
    plt.title('Histogram of Generated Random Numbers')
    
    # Return the time taken and the matplotlib Axes object
    return (time_taken, plt.gca())