
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def task_func(data):
    # Normalize the counts using z-score normalization
    z_scores = zscore(data['counts'])
    norm_counts = z_scores / z_scores.max()

    # Normalize the weights using min-max scaling
    scaler = MinMaxScaler()
    norm_weights = scaler.fit_transform(data['weights'])

    # Create a DataFrame with the normalized counts and weights
    df = pd.DataFrame({
        'Item': data['items'],
        'Normalized Count': norm_counts,
        'Normalized Weight': norm_weights
    })

    return df