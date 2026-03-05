
import random
import bisect
import statistics
import matplotlib.pyplot as plt

def task_func(n, value):
    # Generate 'n' random numbers between 0 and 1
    numbers = [random.random() for i in range(n)]

    # Find the average of the numbers
    average = statistics.mean(numbers)

    # Find the numbers greater than the average
    greater_than_average = [x for x in numbers if x > average]

    # Count the number of numbers greater than or equal to the specified value
    count = len([x for x in greater_than_average if x >= value])

    # Sort the numbers
    sorted_numbers = sorted(greater_than_average)

    # Plot the sorted numbers
    plt.plot(sorted_numbers)

    return sorted_numbers, count