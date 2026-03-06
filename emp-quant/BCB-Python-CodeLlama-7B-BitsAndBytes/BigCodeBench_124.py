
from random import randint, seed as random_seed
import time
import matplotlib.pyplot as plt

def task_func(my_list, size=100, seed=100):
    # Check if 'my_list' is a list
    if not isinstance(my_list, list):
        raise TypeError("'my_list' must be a list")

    # Check if 'my_list' contains only numeric elements (int or float)
    for element in my_list:
        if not isinstance(element, (int, float)):
            raise ValueError("'my_list' must contain only numeric elements")

    # Append 12 to 'my_list'
    my_list.append(12)

    # Generate a list of random integers based on the sum of elements in 'my_list'
    random_seed(seed)
    random_ints = [randint(1, 100) for _ in range(sum(my_list))]

    # Limit the size of the random integers list to 'size'
    random_ints = random_ints[:size]

    # Measure the time taken to generate the list
    start_time = time.time()
    for i in range(1000):
        random_ints = [randint(1, 100) for _ in range(sum(my_list))]
    end_time = time.time()
    time_taken = end_time - start_time

    # Plot a histogram of the generated random numbers
    fig, ax = plt.subplots()
    ax.hist(random_ints, bins=100, range=(1, 100))
    ax.set_xlabel('Number')
    ax.set_ylabel('Frequency')
    ax.set_title('Histogram of Random Integers')

    # Return the time taken and the matplotlib Axes object for the histogram
    return (time_taken, ax)