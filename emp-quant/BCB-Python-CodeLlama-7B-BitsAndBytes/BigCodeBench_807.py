
import numpy as np
from scipy.stats import norm

def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    """
    Determine the outlier indices in a 1D numpy array based on the Z score.

    Parameters
    ----------
    data : np.ndarray
        The input data.
    threshold : float, optional
        The threshold value for the Z score. Default is 2.0.

    Returns
    -------
    outliers : list
        The indices of outliers in the data where Z score > threshold. Empty if standard deviation is 0.
    mean : float
        The mean of the fitted normal distribution.
    var : float
        The variance of the fitted normal distribution.
    """
    # Calculate the mean and standard deviation of the data
    mean = data.mean()
    var = data.var()

    # Check if standard deviation is 0, if so return empty list
    if var == 0:
        return [], mean, var

    # Calculate the Z scores for each data point
    z_scores = (data - mean) / var

    # Find the indices of the outliers
    outliers = [i for i, z in enumerate(z_scores) if abs(z) > threshold]

    return outliers, mean, var