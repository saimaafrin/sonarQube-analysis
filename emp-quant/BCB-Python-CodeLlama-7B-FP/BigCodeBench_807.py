import numpy as np
from scipy.stats import norm
def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    """
    Determine the outlier indices in a 1D numpy array based on the Z score.
    First a normal distribution is fitted to the data, the mean and standard deviation is used to calculate the z scores of each datapoint.
    If the absolute z score of a datapoint is larger than threshold it is considered an outlier and its index is recorded.
    If the standard deviation is 0, an empty list is returned as outliers.
    """
    # Check if standard deviation is 0
    if np.std(data) == 0:
        return []

    # Fit a normal distribution to the data
    mean, var = norm.fit(data)

    # Calculate Z scores for each datapoint
    z_scores = (data - mean) / np.sqrt(var)

    # Identify outliers based on Z score
    outliers = [i for i, z in enumerate(z_scores) if abs(z) > threshold]

    return outliers, mean, var
data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])