
import random
import matplotlib.pyplot as plt

def task_func(points: int):
    # Generate a list of random numbers
    numbers = [random.random() for _ in range(points)]

    # Create a matplotlib figure and axis
    fig, ax = plt.subplots()

    # Plot the random numbers on the axis
    ax.plot(range(points), numbers)

    # Set the title and labels
    ax.set_title("Random Numbers")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")

    # Return the list of numbers and the matplotlib Axes object
    return numbers, ax

# Call the function with 100 points
numbers, ax = task_func(100)

# Show the plot
plt.show()