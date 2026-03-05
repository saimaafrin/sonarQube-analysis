
import numpy as np
from scipy.stats import norm

def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    # Check if standard deviation is 0
    if np.std(data) == 0:
        return [], np.mean(data), np.var(data)
    
    # Fit a normal distribution to the data
    mean = np.mean(data)
    std = np.std(data)
    
    # Calculate the z-scores
    z_scores = np.abs((data - mean) / std)
    
    # Find the indices of outliers
    outliers = np.where(z_scores > threshold)[0]
    
    return outliers.tolist(), mean, std**2