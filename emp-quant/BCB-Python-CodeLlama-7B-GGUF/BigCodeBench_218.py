
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'
def task_func(df, dict_mapping, plot_histogram=False):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    # Check if FEATURES and TARGET columns are in the input DataFrame
    if not all(col in df.columns for col in [FEATURES, TARGET]):
        raise ValueError("FEATURES and TARGET columns not in the input DataFrame")
    # Replace values according to dict_mapping
    df[FEATURES] = df[FEATURES].replace(dict_mapping)
    # Standardize specified features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])
    # Draw histogram of target variable if plot_histogram is True
    if plot_histogram:
        import matplotlib.pyplot as plt
        plt.hist(df[TARGET])
        plt.show()
    return df, None