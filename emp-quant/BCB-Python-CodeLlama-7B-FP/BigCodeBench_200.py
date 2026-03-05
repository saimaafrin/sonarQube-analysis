import random
import bisect
import statistics
import matplotlib.pyplot as plt
def task_func(n, value):
    """
    Generates 'n' random numbers between 0 and 1, finds those greater than their average, and counts how many are greater than or equal to a specified value, then plots the sorted numbers.
    The function should output with:
        list: Numbers greater than the average of all generated numbers.
        int: The count of numbers greater than or equal to the specified value.
    """
    # Generate 'n' random numbers between 0 and 1
    numbers = [random.random() for _ in range(n)]

    # Calculate the average of the numbers
    average = statistics.mean(numbers)

    # Find the numbers greater than the average
    greater_than_average = [number for number in numbers if number > average]

    # Count the numbers greater than or equal to the specified value
    count = sum(1 for number in greater_than_average if number >= value)

    # Sort the numbers
    sorted_numbers = sorted(greater_than_average)

    # Plot the sorted numbers
    plt.plot(sorted_numbers)

    # Return the list of numbers greater than the average and the count
    return greater_than_average, count
n = 100
value = 0.5