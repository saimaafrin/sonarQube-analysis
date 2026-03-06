
import numpy as np
from scipy import stats

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']

def task_func(df, dct):
    # Check if input is valid
    if 'feature1' not in df.columns:
        return 'Invalid input'

    # Replace values in the DataFrame based on the dictionary
    for feature in FEATURES:
        if feature in dct:
            df[feature] = df[feature].replace(dct[feature])

    # Calculate statistics for each feature
    stats_dict = {}
    for feature in FEATURES:
        stats_dict[feature] = {}
        stats_dict[feature]['mean'] = df[feature].mean()
        stats_dict[feature]['median'] = df[feature].median()
        stats_dict[feature]['mode'] = df[feature].mode()
        stats_dict[feature]['variance'] = df[feature].var()

    return stats_dict