import numpy as np
from scipy import stats
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
def task_func(df, dct):
    # Check if the input DataFrame contains the required features
    if not all(feature in df.columns for feature in FEATURES):
        return "Invalid input"
    
    # Replace values in the DataFrame based on the provided dictionary mapping
    for feature in FEATURES:
        if feature in dct:
            df[feature] = df[feature].replace(dct[feature])
    
    # Initialize a dictionary to store the results
    results = {}
    
    # Calculate and store the mean, median, mode, and variance for each feature
    for feature in FEATURES:
        try:
            mean = np.mean(df[feature])
            median = np.median(df[feature])
            mode = stats.mode(df[feature])[0][0]
            variance = np.var(df[feature])
            results[feature] = {'mean': mean, 'median': median, 'mode': mode, 'variance': variance}
        except Exception as e:
            return "Invalid input"
    
    return results