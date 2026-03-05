
from itertools import cycle
from random import choice, seed

def task_func(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    if n_colors <= 0:
        return []
    if rng_seed:
        seed(rng_seed)
    color_pattern = []
    for i in range(n_colors):
        if i % 2 == 0:
            color_pattern.append(colors[i % len(colors)])
        else:
            color_pattern.append(choice(colors))
    return color_pattern