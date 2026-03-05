
import numpy as np
from scipy.stats import norm

def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    # Fit a normal distribution to the data
    mean, var = norm.fit(data)

    # Calculate the z scores for each datapoint
    z_scores = (data - mean) / var

    # Identify outliers
    outliers = [i for i, z in enumerate(z_scores) if abs(z) > threshold]

    return outliers, mean, var