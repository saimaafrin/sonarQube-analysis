
import numpy as np
from scipy.stats import norm

def task_func(data: np.ndarray, threshold: float = 2.0) -> list:
    if np.std(data) == 0:
        return [], np.mean(data), np.var(data)
    
    mean = np.mean(data)
    std_dev = np.std(data)
    z_scores = [(x - mean) / std_dev for x in data]
    outliers = [index for index, z_score in enumerate(z_scores) if abs(z_score) > threshold]
    
    return outliers, mean, std_dev**2