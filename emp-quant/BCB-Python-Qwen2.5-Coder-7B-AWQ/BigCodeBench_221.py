import numpy as np
from scipy import stats
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
def task_func(df, dct):
    result = {}
    for feature in FEATURES:
        if feature not in df.columns:
            return "Invalid input"
        try:
            # Replace values in the DataFrame based on the provided dictionary mapping
            df[feature] = df[feature].replace(dct.get(feature, {}))
            
            # Calculate mean, median, mode, and variance
            mean = np.mean(df[feature])
            median = np.median(df[feature])
            mode = stats.mode(df[feature])[0][0]
            variance = np.var(df[feature])
            
            result[feature] = {
                'mean': mean,
                'median': median,
                'mode': mode,
                'variance': variance
            }
        except Exception as e:
            return "Invalid input"
    return result