import numpy as np
from scipy import stats
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
def task_func(df, dct):
    # Check if the required 'feature1' key is present in the DataFrame
    if 'feature1' not in df.columns:
        return "Invalid input"
    
    # Initialize the result dictionary
    result = {}
    
    # Iterate over each feature in the FEATURES list
    for feature in FEATURES:
        if feature not in df.columns:
            result[feature] = "Invalid input"
            continue
        
        # Replace values in the DataFrame based on the provided dictionary mapping
        df[feature] = df[feature].replace(dct)
        
        # Calculate mean, median, mode, and variance
        try:
            mean = np.mean(df[feature])
            median = np.median(df[feature])
            mode = stats.mode(df[feature])[0][0]
            variance = np.var(df[feature])
            
            # Store the results in the dictionary
            result[feature] = {
                'mean': mean,
                'median': median,
                'mode': mode,
                'variance': variance
            }
        except Exception as e:
            result[feature] = "Error in calculation"
    
    return result