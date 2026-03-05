from itertools import cycle
from random import choice, seed
def task_func(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    """
    Generates a list representing a color pattern. The pattern consists of 'n_colors' elements and alternates
    between a cyclic sequence of colors as defined in the parameter 'colors', and random colors from the same list.
    Optionally, a seed for the random number generator can be provided for repeatable randomness.
    If n_colors is smaller than or equal to zero an empty list is returned.
    
    :param n_colors: Number of colors in the pattern
    :param colors: List of colors to use in the pattern
    :param rng_seed: Seed for the random number generator for repeatable results
    :return: List of colors representing the pattern
    """
    if n_colors <= 0:
        return []
    
    if rng_seed is not None:
        seed(rng_seed)
    
    color_cycle = cycle(colors)
    color_pattern = []
    
    for _ in range(n_colors):
        color_pattern.append(next(color_cycle))
        color_pattern.append(choice(colors))
    
    return color_pattern[:n_colors]
colors = ['Brown', 'Green', 'Black']