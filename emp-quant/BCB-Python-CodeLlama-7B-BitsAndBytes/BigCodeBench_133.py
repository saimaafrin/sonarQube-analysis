
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    if df.empty:
        raise ValueError("DataFrame is empty")

    # Normalize the last column of the DataFrame
    scaler = MinMaxScaler()
    df_normalized = scaler.fit_transform(df.iloc[:, -1].values.reshape(-1, 1))

    # Create a new DataFrame with the normalized data
    df_normalized = pd.DataFrame(df_normalized, columns=['normalized'])
    df_normalized.index = df.index

    # Plot the normalized data
    fig, ax = plt.subplots()
    ax.plot(df_normalized.index, df_normalized['normalized'])
    ax.set_title('Normalized Data of {}'.format(df.columns[-1]))
    ax.set_xlabel('Index')
    ax.set_ylabel('Normalized Value')
    plt.show()

    return df_normalized, ax