
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
# Constants
COLUMNS = ['Date', 'Value']
def task_func(df, plot=False):
    # Check if the DataFrame has the required columns
    if not all(col in df.columns for col in COLUMNS):
        raise KeyError(f"The DataFrame must have the columns '{', '.join(COLUMNS)}'")
    
    # Convert the 'Date' column to datetime
    df['Date'] = pd.to_datetime(df['Date'])
    
    # Set the index to 'Date'
    df.set_index('Date', inplace=True)
    
    # Split the 'Value' column into separate columns
    df = pd.DataFrame(df['Value'].str.split(',').tolist(), index=df.index)
    
    # Scale the values using StandardScaler
    scaler = StandardScaler()
    scaled_values = scaler.fit_transform(df)
    
    # Create a new DataFrame with the scaled values
    scaled_df = pd.DataFrame(scaled_values, columns=df.columns, index=df.index)
    
    # Optionally plot the scaled values
    if plot:
        fig, ax = plt.subplots()
        ax.bar(scaled_df.index, scaled_df.iloc[:, 0], label='Scaled Value')
        ax.set_xlabel('Date')
        ax.set_ylabel('Scaled Value')
        ax.set_title('Scaled Values Over Time')
        return fig, ax
    else:
        return scaled_df