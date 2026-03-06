
import pandas as pd
from sklearn.preprocessing import StandardScaler
# Constants
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'

def task_func(df, dict_mapping, plot_histogram=False):
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame")

    # Check if FEATURES and TARGET columns are in the input DataFrame
    if not all([col in df.columns for col in FEATURES + [TARGET]]):
        raise ValueError("FEATURES and TARGET columns not in the input DataFrame")

    # Replace values according to dict_mapping
    for col in FEATURES:
        df[col] = df[col].replace(dict_mapping)

    # Standardize features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])

    # Draw histogram of target variable if plot_histogram is True
    if plot_histogram:
        import matplotlib.pyplot as plt
        plt.hist(df[TARGET])
        plt.xlabel("Target variable")
        plt.ylabel("Frequency")
        plt.title("Histogram of target variable")
        plt.show()

    return df, None

dict_mapping = {
    'feature1': {1: 0, 2: 1, 3: 2},
    'feature2': {6: 0, 7: 1, 8: 2},
    'feature3': {11: 0, 12: 1, 13: 2},
    'feature4': {16: 0, 17: 1, 18: 2},
    'feature5': {21: 0, 22: 1, 23: 2}
}

df, axes = task_func(df, dict_mapping, plot_histogram=True)
print(df)