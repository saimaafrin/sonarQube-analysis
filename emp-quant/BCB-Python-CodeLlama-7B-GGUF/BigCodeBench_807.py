
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
        The threshold for the Z score. Default is 2.0.

    Returns
    -------
    outliers : list
        The indices of outliers in the data where Z score > threshold. Empty if standard deviation is 0.
    mean : float
        The mean of the fitted normal distribution.
    var : float
        The variance of the fitted normal distribution.
    """
    if np.std(data) == 0:
        return [], 0, 0

    mean, var = norm.fit(data)
    z_scores = np.abs(norm.ppf(data, loc=mean, scale=np.sqrt(var)))
    outliers = np.where(z_scores > threshold)[0].tolist()

    return outliers, mean, var

data = np.array([-10, 3, 5, 5, 5, 5, 5, 7, 20])
outliers, mean, var = task_func(data, threshold=4)
print(outliers)  # []
print(mean)  # 5.0
print(var)  # 50.888888888888886