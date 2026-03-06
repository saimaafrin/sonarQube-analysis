import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
PLOT_TITLE = "Scaled Values"
def task_func(data_dict):
    """
    Scales the values in a given dictionary using MinMaxScaler and plots the scaled data.

    Parameters:
    - data_dict (dict): A dictionary where keys represent column names and values are lists of numerical data.
                        The values may contain missing data (None), which are handled by dropping them before scaling.

    Returns:
    - pandas.DataFrame containing the scaled data.
    - matplotlib Axes object that displays the plot of the scaled data.

    Requirements:
    - pandas
    - scikit-learn
    - matplotlib

    Example:
    >>> data = {'a': [1, 2, None, 4], 'b': [5, None, 7, 8]}
    >>> scaled_df, plot_ax = task_func(data)
    >>> scaled_df
         a    b
    0  0.0  0.0
    1  1.0  1.0
    >>> plot_ax.get_title()
    'Scaled Values'
    """
    # Create a dataframe from the dictionary
    df = pd.DataFrame(data_dict)

    # Drop missing values
    df = df.dropna()

    # Create a MinMaxScaler object
    scaler = MinMaxScaler()

    # Scale the data
    scaled_df = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    # Plot the scaled data
    plot_ax = scaled_df.plot(title=PLOT_TITLE)

    return scaled_df, plot_ax