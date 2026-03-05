
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def task_func(df, dict_mapping, plot_histogram=False):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Check if features and target columns are present in the DataFrame
    if not all(c in df.columns for c in FEATURES + [TARGET]):
        raise ValueError("Features and target columns not in the input DataFrame")

    # Replace values in the DataFrame according to the dict_mapping
    for col in FEATURES:
        if col in dict_mapping:
            df[col] = df[col].map(dict_mapping[col])

    # Standardize the features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])

    # Draw histogram of the target variable if plot_histogram is True
    if plot_histogram:
        import matplotlib.pyplot as plt
        plt.hist(df[TARGET])

    return df