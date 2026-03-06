
import numpy as np
from scipy import stats

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def task_func(df, dct):
    result = {}
    
    # Check if the required keys exist in the DataFrame
    for feature in FEATURES:
        if feature not in df.columns:
            return "Invalid input"
    
    # Replace values in the DataFrame based on the provided dictionary mapping
    try:
        df.replace(dct, inplace=True)
    except Exception as e:
        return str(e)
    
    # Calculate mean, median, mode, and variance for each feature
    for feature in FEATURES:
        try:
            mean = df[feature].mean()
            median = df[feature].median()
            mode = stats.mode(df[feature])[0][0]
            variance = df[feature].var()
            
            result[feature] = {
                'mean': mean,
                'median': median,
                'mode': mode,
                'variance': variance
            }
        except Exception as e:
            result[feature] = str(e)
    
    return result