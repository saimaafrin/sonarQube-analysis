from itertools import cycle
from random import choice, seed
def task_func(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    """
    Generates a list representing a color pattern. The pattern consists of 'n_colors' elements and alternates between a cyclic sequence of colors as defined in the parameter 'colors', and random colors from the same list. Optionally, a seed for the random number generator can be provided for repeatable randomness. If n_colors is smaller than or equal to zero an empty list is returned.
    """
    if n_colors <= 0:
        return []
    if rng_seed is not None:
        seed(rng_seed)
    color_pattern = []
    for i in range(n_colors):
        if i % 2 == 0:
            color_pattern.append(colors[i % len(colors)])
        else:
            color_pattern.append(choice(colors))
    return color_pattern
colors = ['Brown', 'Green', 'Black']