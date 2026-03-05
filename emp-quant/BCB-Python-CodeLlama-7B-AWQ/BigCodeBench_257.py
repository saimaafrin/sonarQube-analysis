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
    end_angle = 360 * num_turns

    # Set the radial ticks
    radial_ticks = np.linspace(start_angle, end_angle, num_turns * 45)

    # Set the radial tick labels
    radial_tick_labels = [f"{i}°" for i in radial_ticks]

    # Draw the spiral
    ax.plot(radial_ticks, np.zeros(len(radial_ticks)), 'o-')

    # Set the radial tick labels
    ax.set_xticklabels(radial_tick_labels)

    # Set the radial tick positions
    ax.set_xticks(radial_ticks)

    # Set the radial tick label rotation
    ax.set_xticklabels(radial_tick_labels, rotation=45)

    # Set the title
    ax.set_title("Spiral Plot")

    # Return the modified Axes object
    return ax