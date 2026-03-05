import random
import bisect
import statistics
import matplotlib.pyplot as plt
def task_func(n, value):
    """
    Generates 'n' random numbers between 0 and 1, finds those greater than their average, and counts how many are greater than or equal to a specified value, then plots the sorted numbers.
    Returns a list of numbers greater than the average of all generated numbers and the count of numbers greater than or equal to the specified value.
    """
    # Generate 'n' random numbers between 0 and 1
    numbers = [random.random() for _ in range(n)]

    # Calculate the average of the generated numbers
    average = statistics.mean(numbers)

    # Find the numbers greater than the average
    greater_than_average = [number for number in numbers if number > average]

    # Count the number of numbers greater than or equal to the specified value
    count = len([number for number in greater_than_average if number >= value])

    # Sort the numbers and plot them
    sorted_numbers = sorted(greater_than_average)
    plt.plot(sorted_numbers)

    return greater_than_average, count
n = 100
value = 0.5