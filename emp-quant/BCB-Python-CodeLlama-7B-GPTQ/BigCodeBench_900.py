import pandas as pd
import numpy as np
def task_func(d):
    """
    Calculate mean, sum, max, min, and standard deviation for the keys "x", "y", and "z" from a list of dictionaries "d".
    The function should raise the exception for: ValueError: If input is not a list of dictionaries.
    The function should output with:
        dict: A dictionary with keys as 'x', 'y', and 'z' and values as dictionaries of statistics.
    """
    if not isinstance(d, list):
        raise ValueError("Input must be a list of dictionaries.")
    if not all(isinstance(item, dict) for item in d):
        raise ValueError("Input must be a list of dictionaries.")

    # Calculate statistics for each key
    x_stats = pd.DataFrame(d).groupby("x").agg(
        mean=("x", np.mean),
        sum=("x", np.sum),
        max=("x", np.max),
        min=("x", np.min),
        std=("x", np.std),
    )
    y_stats = pd.DataFrame(d).groupby("y").agg(
        mean=("y", np.mean),
        sum=("y", np.sum),
        max=("y", np.max),
        min=("y", np.min),
        std=("y", np.std),
    )
    z_stats = pd.DataFrame(d).groupby("z").agg(
        mean=("z", np.mean),
        sum=("z", np.sum),
        max=("z", np.max),
        min=("z", np.min),
        std=("z", np.std),
    )

    # Combine statistics into a single dictionary
    stats = {
        "x": x_stats,
        "y": y_stats,
        "z": z_stats,
    }

    return stats
d = [
    {"x": 1, "y": 2, "z": 3},
    {"x": 4, "y": 5, "z": 6},
    {"x": 7, "y": 8, "z": 9},
]