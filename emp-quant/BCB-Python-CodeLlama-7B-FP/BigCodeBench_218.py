import pandas as pd
from sklearn.preprocessing import StandardScaler
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'
def task_func(df, dict_mapping, plot_histogram=False):
    """
    Pre-processes a DataFrame by replacing values according to a dictionary mapping, standardizing specified features, and optionally drawing a histogram of the target variable.
    The function should raise the exception for:
        - The function will raise ValueError if the FEATURES and TARGET columns not in the input DataFrame.
        - The function will raise ValueError if the input df is not a DataFrame.
    The function should output with:
        - DataFrame: The preprocessed DataFrame with standardized features and values replaced as per dict_mapping.
        - Axes: The histogram of the target variable if plot_histogram is True, otherwise None.
    """
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame")

    # Check if FEATURES and TARGET columns are in the input DataFrame
    if not all(col in df.columns for col in [FEATURES, TARGET]):
        raise ValueError("FEATURES and TARGET columns must be in the input DataFrame")

    # Replace values according to dict_mapping
    df = df.replace(dict_mapping)

    # Standardize specified features
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
df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [6, 7, 8, 9, 10],
    'feature3': [11, 12, 13, 14, 15],
    'feature4': [16, 17, 18, 19, 20],
    'feature5': [21, 22, 23, 24, 25],
    'target': [26, 27, 28, 29, 30]
})
dict_mapping = {
    'feature1': {1: 0, 2: 1, 3: 2},
    'feature2': {6: 0, 7: 1, 8: 2},
    'feature3': {11: 0, 12: 1, 13: 2},
    'feature4': {16: 0, 17: 1, 18: 2},
    'feature5': {21: 0, 22: 1, 23: 2}
}