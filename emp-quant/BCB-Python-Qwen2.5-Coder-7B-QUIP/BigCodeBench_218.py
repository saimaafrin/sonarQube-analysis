
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def task_func(df, dict_mapping, plot_histogram=False):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame")
    
    # Check if the required columns are present
    if not all(feature in df.columns for feature in FEATURES) or TARGET not in df.columns:
        raise ValueError("The function will raise ValueError if the FEATURES and TARGET columns not in the input DataFrame")
    
    # Replace values according to the dictionary mapping
    df[FEATURES] = df[FEATURES].replace(dict_mapping)
    
    # Standardize specified features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])
    
    # Optionally draw a histogram of the target variable
    axes = None
    if plot_histogram:
        axes = df[TARGET].plot(kind='hist', bins=30, figsize=(8, 6))
    
    return df, axes