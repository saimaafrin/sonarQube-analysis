
import numpy as np
from scipy import stats

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def task_func(df, dct):
    try:
        # Replace values in the DataFrame based on the provided dictionary mapping
        df.replace(dct, inplace=True)
        
        # Initialize a dictionary to store the results
        results = {}
        
        # Calculate statistics for each feature
        for feature in FEATURES:
            if feature in df.columns:
                # Calculate mean
                mean = np.mean(df[feature])
                # Calculate median
                median = np.median(df[feature])
                # Calculate mode
                mode = stats.mode(df[feature])[0][0]
                # Calculate variance
                variance = np.var(df[feature])
                
                # Store the results in the dictionary
                results[feature] = {
                    'mean': mean,
                    'median': median,
                    'mode': mode,
                    'variance': variance
                }
            else:
                return "Invalid input"
        
        return results
    except Exception as e:
        return str(e)