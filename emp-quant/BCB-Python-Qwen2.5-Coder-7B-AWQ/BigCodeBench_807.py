import numpy as np
from scipy.stats import norm
def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    """
    Determine the outlier indices in a 1D numpy array based on the Z score.
    
    Parameters:
    - data: numpy.ndarray - The input data array.
    - threshold: float - The threshold for Z score to consider a point as an outlier.
    
    Returns:
    - list: The indices of outliers in the data where Z score > threshold. Empty if standard deviation is 0.
    - float: The mean of the fitted normal distribution.
    - float: The variance of the fitted normal distribution.
    """
    if np.std(data) == 0:
        return [], np.mean(data), 0
    
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = np.abs((data - mean) / std_dev)
    outliers = np.where(z_scores > threshold)[0].tolist()
    
    return outliers, mean, std_dev**2
data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])