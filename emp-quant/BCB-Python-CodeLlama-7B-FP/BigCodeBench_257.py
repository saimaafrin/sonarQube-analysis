import numpy as np
import math
import matplotlib.pyplot as plt
def task_func(ax, num_turns):
    """
    Draws a spiral on the polar diagram 'ax' with the specified number of turns 'num_turns'.
    The spiral starts at the center and expands outward with each turn.
    The radial ticks on the plot are positioned at intervals corresponding to the number of turns multiplied by 45 degrees.
    """
    # Set the number of turns
    num_turns = int(num_turns)

    # Set the starting angle
    start_angle = 0

    # Set the ending angle
    end_angle = 2 * math.pi * num_turns

    # Set the radial ticks
    radial_ticks = np.linspace(start_angle, end_angle, num_turns * 45)

    # Draw the spiral
    ax.plot(radial_ticks, radial_ticks, 'o-')

    # Set the axis labels
    ax.set_xlabel('Radial Ticks')
    ax.set_ylabel('Angular Ticks')

    # Set the title
    ax.set_title('Spiral Plot')

    # Return the modified Axes object
    return ax