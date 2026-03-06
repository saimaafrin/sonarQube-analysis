
from itertools import cycle
from random import choice, seed

def task_func(n_colors, colors=['Red', 'Green', 'Blue', 'Yellow', 'Purple'], rng_seed=None):
    if n_colors <= 0:
        return []
    
    if rng_seed is not None:
        seed(rng_seed)
    
    color_cycle = cycle(colors)
    random_color_list = [choice(colors) for _ in range(n_colors)]
    
    pattern = []
    for i in range(n_colors):
        pattern.append(next(color_cycle))
        pattern.append(random_color_list[i])
    
    return pattern[:n_colors]