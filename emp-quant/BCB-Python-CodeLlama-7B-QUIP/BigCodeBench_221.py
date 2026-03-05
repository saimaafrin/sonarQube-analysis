
import numpy as np
from scipy import stats
# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
def task_func(df, dct):
    # Check input
    if not isinstance(df, pd.DataFrame):
        return "Invalid input"
    if not isinstance(dct, dict):
        return "Invalid input"
    # Replace values
    for feature in FEATURES:
        if feature in dct:
            df[feature] = dct[feature]
    # Calculate statistics
    mean = df.mean()
    median = df.median()
    mode = stats.mode(df)
    variance = df.var()
    # Return dictionary
    return {
        "mean": mean,
        "median": median,
        "mode": mode,
        "variance": variance
    }