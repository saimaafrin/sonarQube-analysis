
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def task_func(data):
    # Normalize the counts using z-score normalization
    zscores = zscore(data['counts'])
    # Normalize the weights using min-max scaling
    scaler = MinMaxScaler()
    weights = scaler.fit_transform(data['weights'].values.reshape(-1, 1))
    # Create a new DataFrame with the normalized counts and weights
    df = pd.DataFrame({'Item': data['items'], 'Normalized Count': zscores, 'Normalized Weight': weights})
    return df