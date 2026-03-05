
import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler

def task_func(data):
    # Normalize counts using z-score normalization
    zscores = zscore(data['count'])
    norm_counts = pd.Series(zscores, index=data.index)

    # Normalize weights using min-max scaling
    scaler = MinMaxScaler()
    norm_weights = scaler.fit_transform(data['weight'])

    # Create a new DataFrame with normalized counts and weights
    output = pd.DataFrame({'Item': data['item'],
                            'Normalized Count': norm_counts,
                            'Normalized Weight': norm_weights})

    return output