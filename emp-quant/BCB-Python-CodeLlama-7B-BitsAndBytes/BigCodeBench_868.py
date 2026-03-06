
from itertools import cycle
from random import choice, seed

def task_func(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    if n_colors <= 0:
        return []
    else:
        if rng_seed is not None:
            seed(rng_seed)
        color_cycle = cycle(colors)
        color_pattern = []
        for i in range(n_colors):
            if i % 2 == 0:
                color_pattern.append(next(color_cycle))
            else:
                color_pattern.append(choice(colors))
        return color_pattern