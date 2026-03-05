import numpy as np
from scipy.stats import norm
def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    """
    Determine the outlier indices in a 1D numpy array based on the Z score.
    
    Parameters:
    - data: A 1D numpy array of numerical data.
    - threshold: A float representing the threshold for Z score to consider a data point as an outlier.
    
    Returns:
    - A list of indices of outliers in the data where Z score > threshold.
    - The mean of the fitted normal distribution.
    - The variance of the fitted normal distribution.
    """
    if np.std(data) == 0:
        return [], np.mean(data), 0.0
    
    z_scores = np.abs(norm.ppf((1 + (1 / (2 * threshold))) / 2) * np.std(data) + np.mean(data) - data)
    outliers = np.where(z_scores > threshold)[0].tolist()
    
    return outliers, np.mean(data), np.var(data)
data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])