
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
COLUMNS = ['Date', 'Value']

def task_func(df, plot=False):
    # Check if the DataFrame has the required columns
    if not all(c in df.columns for c in COLUMNS):
        raise KeyError("DataFrame must have 'Date' and 'Value' columns")

    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])

    # Create a new DataFrame with the scaled values
    scaled_df = pd.DataFrame(index=df.index)
    for col in df.columns:
        if col in COLUMNS:
            scaled_df[col] = StandardScaler().fit_transform(df[col].values.reshape(-1, 1))

    # Plot the scaled values
    if plot:
        fig, ax = plt.subplots()
        ax.bar(df['Date'], scaled_df['Value'])
        ax.set_xlabel('Date')
        ax.set_ylabel('Scaled Value')
        ax.set_title('Scaled Values Over Time')
        return fig, ax

    return scaled_df