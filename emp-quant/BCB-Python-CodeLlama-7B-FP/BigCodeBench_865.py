import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
def task_func(data):
    """
    This function takes a list of tuples containing elements and their respective counts and weights.
    It normalizes the counts using z-score normalization and the weights using min-max scaling.
    Finally, it returns a pandas DataFrame with the items, normalized counts, and normalized weights.
    """
    # Normalize the counts using z-score normalization
    z_scores = zscore(data['counts'])
    # Normalize the weights using min-max scaling
    min_max_scaler = MinMaxScaler()
    scaled_weights = min_max_scaler.fit_transform(data['weights'])
    # Create a DataFrame with the normalized counts and weights
    df = pd.DataFrame({'Item': data['items'],
                       'Normalized Count': z_scores,
                       'Normalized Weight': scaled_weights})
    return df
data = [('apple', 10, 1.0),
        ('banana', 20, 2.0),
        ('orange', 30, 3.0)]