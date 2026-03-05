import pandas as pd
import numpy as np
from scipy.stats import zscore
from sklearn.preprocessing import MinMaxScaler
def task_func(data):
    # Extract items, counts, and weights from the input data
    items = [item for item, count, weight in data]
    counts = [count for item, count, weight in data]
    weights = [weight for item, count, weight in data]
    
    # Normalize counts using z-score normalization
    normalized_counts = zscore(counts)
    
    # Normalize weights using min-max scaling
    scaler = MinMaxScaler()
    normalized_weights = scaler.fit_transform(np.array(weights).reshape(-1, 1)).flatten()
    
    # Create a pandas DataFrame with the results
    result_df = pd.DataFrame({
        'Item': items,
        'Normalized Count': normalized_counts,
        'Normalized Weight': normalized_weights
    })
    
    return result_df