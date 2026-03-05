import numpy as np
from scipy import stats
import pandas as pd
import numpy as np
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
def task_func(df, dct):
    """
    Calculates and returns the mean, median, mode, and variance for specified features in a DataFrame.
    It replaces certain values in the DataFrame based on a provided dictionary mapping before performing the calculations.
    Note that:
        - The function would return "Invalid input" string if the input is invalid (e.g., does not contain the required 'feature1' key) or if there is an error in the calculation.
        - The function should output with:
            dict: A dictionary containing statistics (mean, median, mode, variance) for each feature defined in the 'FEATURES' constant.
    """
    # Check if input is valid
    if not all(feature in df.columns for feature in FEATURES):
        return "Invalid input"
    # Replace values in the DataFrame based on the dictionary mapping
    for feature, value in dct.items():
        if feature in df.columns:
            df[feature] = df[feature].replace(value)
    # Calculate statistics for each feature
    statistics = {}
    for feature in FEATURES:
        try:
            statistics[feature] = {
                "mean": df[feature].mean(),
                "median": df[feature].median(),
                "mode": df[feature].mode(),
                "variance": df[feature].var()
            }
        except:
            return "Invalid input"
    return statistics
data = {
    "feature1": [1, 2, 3, 4, 5],
    "feature2": [6, 7, 8, 9, 10],
    "feature3": [11, 12, 13, 14, 15],
    "feature4": [16, 17, 18, 19, 20],
    "feature5": [21, 22, 23, 24, 25]
}
df = pd.DataFrame(data)
dct = {"feature1": 0, "feature2": 10, "feature3": 20, "feature4": 30, "feature5": 40}