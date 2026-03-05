import pandas as pd
from sklearn.preprocessing import StandardScaler
FEATURES = ['feature1', 'feature2', 'feature3', 'feature4', 'feature5']
TARGET = 'target'
def task_func(df, dict_mapping, plot_histogram=False):
    """
    Pre-processes a DataFrame by replacing values according to a dictionary mapping, standardizing specified features, and optionally drawing a histogram of the target variable.
    
    Parameters:
    - df (pd.DataFrame): The input DataFrame to be preprocessed.
    - dict_mapping (dict): A dictionary mapping values to be replaced in the DataFrame.
    - plot_histogram (bool): Whether to plot a histogram of the target variable.
    
    Returns:
    - pd.DataFrame: The preprocessed DataFrame with standardized features and values replaced as per dict_mapping.
    - Axes: The histogram of the target variable if plot_histogram is True, otherwise None.
    """
    # Check if input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Check if FEATURES and TARGET columns are in the DataFrame
    if not all(col in df.columns for col in [TARGET] + FEATURES):
        raise ValueError("The function will raise ValueError if the FEATURES and TARGET columns not in the input DataFrame.")
    
    # Replace values according to dict_mapping
    df.replace(dict_mapping, inplace=True)
    
    # Standardize specified features
    scaler = StandardScaler()
    df[FEATURES] = scaler.fit_transform(df[FEATURES])
    
    # Optionally draw a histogram of the target variable
    if plot_histogram:
        import matplotlib.pyplot as plt
        return df, plt.hist(df[TARGET], bins=10)
    else:
        return df, None
df = pd.DataFrame({
    'feature1': [1, 2, 3, 4, 5],
    'feature2': [5, 4, 3, 2, 1],
    'feature3': [2, 3, 4, 5, 6],
    'feature4': [6, 5, 4, 3, 2],
    'feature5': [3, 4, 5, 6, 7],
    'target': [0, 1, 0, 1, 0]
})
dict_mapping = {1: 'low', 2: 'medium', 3: 'high', 4: 'very high', 5: 'extreme'}