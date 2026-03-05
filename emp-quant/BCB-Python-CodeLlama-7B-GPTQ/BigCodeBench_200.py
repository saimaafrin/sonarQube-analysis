import random
import bisect
import statistics
import matplotlib.pyplot as plt
def task_func(n, value):
    # Generate 'n' random numbers between 0 and 1
    numbers = [random.random() for _ in range(n)]

    # Find the average of the generated numbers
    average = statistics.mean(numbers)

    # Find the numbers greater than the average
    greater_than_average = [number for number in numbers if number > average]

    # Count the numbers greater than or equal to the specified value
    count = len([number for number in greater_than_average if number >= value])

    # Plot the sorted numbers
    plt.plot(sorted(numbers))

    # Return the list of numbers greater than the average and the count
    return greater_than_average, count
n = 100
value = 0.5