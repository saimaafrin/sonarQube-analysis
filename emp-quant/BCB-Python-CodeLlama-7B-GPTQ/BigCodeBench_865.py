import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
def task_func(data):
    """
    This function takes a list of tuples containing elements and their respective counts and weights. It normalizes the counts using z-score normalization and the weights using min-max scaling. Finally, it returns a pandas DataFrame with the items, normalized counts, and normalized weights.
    """
    # Normalize the counts using z-score normalization
    z_scores = zscore(data.counts)
    # Normalize the weights using min-max scaling
    min_max_scaler = MinMaxScaler()
    min_max_scaler.fit(data.weights)
    min_max_scaled_weights = min_max_scaler.transform(data.weights)
    # Create a new DataFrame with the normalized counts and weights
    normalized_data = pd.DataFrame({
        'Item': data.items,
        'Normalized Count': z_scores,
        'Normalized Weight': min_max_scaled_weights
    })
    return normalized_data
data = pd.DataFrame({
    'items': ['A', 'B', 'C', 'D', 'E'],
    'counts': [10, 20, 30, 40, 50],
    'weights': [0.1, 0.2, 0.3, 0.4, 0.5]
})