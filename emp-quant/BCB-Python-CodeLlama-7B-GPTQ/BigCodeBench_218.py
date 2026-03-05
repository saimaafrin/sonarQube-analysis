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
    # Check if the input df is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("The input df is not a DataFrame.")

    # Check if the FEATURES and TARGET columns are in the input DataFrame
    if not all([col in df.columns for col in [FEATURES, TARGET]]):
        raise ValueError("The FEATURES and TARGET columns not in the input DataFrame.")

    # Replace values according to the dictionary mapping
    df[FEATURES] = df[FEATURES].replace(dict_mapping)

    # Standardize the specified features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])

    # Draw a histogram of the target variable if plot_histogram is True
    if plot_histogram:
        fig, ax = plt.subplots()
        ax.hist(df[TARGET], bins=20)
        return df, ax
    else:
        return df, None
df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [6, 7, 8, 9, 10],
    'feature3': [11, 12, 13, 14, 15],
    'feature4': [16, 17, 18, 19, 20],
    'feature5': [21, 22, 23, 24, 25],
    'target': [26, 27, 28, 29, 30]
})
dict_mapping = {1: 0, 2: 1, 3: 2, 4: 3, 5: 4}