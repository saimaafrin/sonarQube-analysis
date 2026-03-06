
import numpy as np
import math
import matplotlib.pyplot as plt

def task_func(ax, num_turns):
    # Set the number of turns
    num_turns = int(num_turns)

    # Set the starting angle and radius
    start_angle = 0
    start_radius = 0

    # Set the tick interval
    tick_interval = 45

    # Create a list to store the points
    points = []

    # Iterate over the number of turns
    for i in range(num_turns):
        # Calculate the angle and radius for this turn
        angle = start_angle + i * tick_interval
        radius = start_radius + i * tick_interval

        # Add the point to the list
        points.append((angle, radius))

    # Plot the spiral
    ax.plot(points)

    # Set the tick labels
    ax.set_xticks(np.arange(0, 360, tick_interval))
    ax.set_yticks(np.arange(0, 10, tick_interval))

    # Set the tick labels
    ax.set_xticklabels(np.arange(0, 360, tick_interval))
    ax.set_yticklabels(np.arange(0, 10, tick_interval))

    # Return the modified Axes object
    return ax

# Create a figure and axis object
fig, ax = plt.subplots()

# Call the task function with the number of turns
task_func(ax, 5)

# Show the plot
plt.show()