
import random
import matplotlib.pyplot as plt

def task_func(points: int):
    # Generate a list of random numbers
    numbers = [random.randint(0, 100) for i in range(points)]

    # Create a matplotlib figure and axis
    fig, ax = plt.subplots()

    # Plot the generated numbers on the x-axis
    ax.plot(numbers)

    # Return the matplotlib Axes object
    return ax