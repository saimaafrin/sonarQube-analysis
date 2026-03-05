
import numpy as np
from scipy import stats

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def task_func(df, dct):
    # Check if the required 'feature1' key is present in the DataFrame
    if 'feature1' not in df.columns:
        return "Invalid input"

    # Replace values in the DataFrame based on the provided dictionary mapping
    for key, value in dct.items():
        df[key] = df[key].replace(value, np.nan)

    # Initialize a dictionary to store the results
    results = {}

    # Iterate over the features and calculate the required statistics
    for feature in FEATURES:
        if feature in df.columns:
            # Calculate mean, median, mode, and variance
            try:
                mean = df[feature].mean()
                median = df[feature].median()
                mode = stats.mode(df[feature])[0][0]
                variance = df[feature].var()
                results[feature] = {'mean': mean, 'median': median, 'mode': mode, 'variance': variance}
            except Exception as e:
                results[feature] = {'mean': np.nan, 'median': np.nan, 'mode': np.nan, 'variance': np.nan}
                print(f"Error calculating statistics for {feature}: {e}")
        else:
            results[feature] = {'mean': np.nan, 'median': np.nan, 'mode': np.nan, 'variance': np.nan}

    return results