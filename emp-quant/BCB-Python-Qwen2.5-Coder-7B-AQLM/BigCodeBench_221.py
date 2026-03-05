
import numpy as np
from scipy import stats

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def task_func(df, dct):
    try:
        # Replace values in the DataFrame based on the provided dictionary mapping
        df.replace(dct, inplace=True)
        
        # Initialize a dictionary to store the statistics
        statistics = {}
        
        # Calculate and store the statistics for each feature
        for feature in FEATURES:
            if feature in df.columns:
                data = df[feature].dropna()
                mean = np.mean(data)
                median = np.median(data)
                mode = stats.mode(data)[0][0]
                variance = np.var(data)
                statistics[feature] = {'mean': mean, 'median': median, 'mode': mode, 'variance': variance}
            else:
                return "Invalid input"
        
        return statistics
    except Exception as e:
        return str(e)