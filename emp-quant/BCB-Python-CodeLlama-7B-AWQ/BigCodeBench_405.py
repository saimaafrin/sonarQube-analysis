import random
import matplotlib.pyplot as plt
def task_func(points: int):
    """
    Generate a plot of random numbers such that indices are on the x-axis and generated numbers are on the y-axis.

    Args:
        points (int): The number of points to generate.

    Returns:
        A list of generated random numbers.
        A matplotlib Axes object representing the plot.
    """
    # Generate random numbers
    numbers = [random.random() for _ in range(points)]

    # Create a figure and axis
    fig, ax = plt.subplots()

    # Plot the numbers
    ax.plot(numbers)

    # Set the title and labels
    ax.set_title('Random Numbers')
    ax.set_xlabel('Index')
    ax.set_ylabel('Value')

    # Return the list of numbers and the axis
    return numbers, ax
points = 10