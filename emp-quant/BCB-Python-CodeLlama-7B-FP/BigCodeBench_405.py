import random
import matplotlib.pyplot as plt
def task_func(points: int):
    """
    Generate a plot of random numbers such that indices are on the x-axis and generated numbers are on the y-axis.
    Returns a tuple containing:
    A list of generated random numbers.
    A matplotlib Axes object representing the plot.
    """
    # Generate random numbers
    numbers = [random.random() for _ in range(points)]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the numbers
    ax.plot(numbers)

    # Set the x-axis label
    ax.set_xlabel('Index')

    # Set the y-axis label
    ax.set_ylabel('Random Number')

    # Return the list of numbers and the axis
    return numbers, ax
points = 10