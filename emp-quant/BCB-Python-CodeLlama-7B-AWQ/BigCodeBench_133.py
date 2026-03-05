import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
def task_func(df):
    """
    Normalize the last column of the DataFrame using MinMaxScaler from sklearn and plot the normalized data.
    The function should raise the exception for: ValueError: If the input is not a DataFrame or if the DataFrame is empty.
    The function should output with:
        DataFrame: A pandas DataFrame where the last column has been normalized.
        Axes: A Matplotlib Axes object representing the plot of the normalized last column. The plot includes:
            Title: 'Normalized Data of <column_name>'
            X-axis label: 'Index'
            Y-axis label: 'Normalized Value'
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Normalize the last column of the DataFrame using MinMaxScaler
    scaler = MinMaxScaler()
    df_normalized = scaler.fit_transform(df)

    # Plot the normalized data
    fig, ax = plt.subplots()
    ax.plot(df_normalized.index, df_normalized.iloc[:, -1])
    ax.set_title(f"Normalized Data of {df.columns[-1]}")
    ax.set_xlabel("Index")
    ax.set_ylabel("Normalized Value")
    plt.show()

    return df_normalized, ax
df = pd.DataFrame({"A": [1, 2, 3, 4, 5], "B": [2, 4, 6, 8, 10]})