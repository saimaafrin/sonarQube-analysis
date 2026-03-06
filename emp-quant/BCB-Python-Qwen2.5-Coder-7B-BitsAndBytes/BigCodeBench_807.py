
import numpy as np
from scipy.stats import norm

def task_func(data: np.ndarray, threshold: float = 2.0) -> tuple:
    # Check if the standard deviation is zero
    if np.std(data) == 0:
        return [], None, None
    
    # Fit a normal distribution to the data
    mu, std = norm.fit(data)
    
    # Calculate the Z-scores for each data point
    z_scores = np.abs((data - mu) / std)
    
    # Find indices where the Z-score is greater than the threshold
    outliers = np.where(z_scores > threshold)[0]
    
    return outliers.tolist(), mu, std**2