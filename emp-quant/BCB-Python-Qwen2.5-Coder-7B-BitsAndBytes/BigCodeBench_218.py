
import pandas as pd
from sklearn.preprocessing import StandardScaler

# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def task_func(df, dict_mapping, plot_histogram=False):
    """
    Pre-processes a DataFrame by replacing values according to a dictionary mapping,
    standardizing specified features, and optionally drawing a histogram of the target variable.

    Parameters:
    - df (pd.DataFrame): Input DataFrame containing the data.
    - dict_mapping (dict): Dictionary mapping old values to new values for replacement.
    - plot_histogram (bool): Whether to draw a histogram of the target variable.

    Returns:
    - pd.DataFrame: The preprocessed DataFrame with standardized features and values replaced as per dict_mapping.
    - Axes: The histogram of the target variable if plot_histogram is True, otherwise None.
    """
    
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")
    
    # Check if required columns are present
    if not all(col in df.columns for col in [TARGET] + FEATURES):
        raise ValueError(f"DataFrame must contain columns {FEATURES} and {TARGET}.")
    
    # Replace values according to the dictionary mapping
    df.replace(dict_mapping, inplace=True)
    
    # Standardize specified features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])
    
    # Optionally draw a histogram of the target variable
    if plot_histogram:
        import matplotlib.pyplot as plt
        return df, df[TARGET].hist(bins=20)
    else:
        return df, None