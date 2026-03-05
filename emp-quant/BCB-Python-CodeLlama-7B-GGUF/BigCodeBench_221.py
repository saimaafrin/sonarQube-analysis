
import numpy as np
from scipy import stats
# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
def task_func(df, dct):
    # Check if input is valid
    if not all(feature in df.columns for feature in FEATURES):
        return "Invalid input"
    # Replace values in the DataFrame based on the dictionary
    for feature, value in dct.items():
        if feature in df.columns:
            df[feature] = df[feature].replace(value)
    # Calculate statistics for each feature
    statistics = {}
    for feature in FEATURES:
        try:
            statistics[feature] = {
                'mean': df[feature].mean(),
                'median': df[feature].median(),
                'mode': df[feature].mode(),
                'variance': df[feature].var()
            }
        except:
            statistics[feature] = "Invalid input"
    return statistics