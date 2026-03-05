
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler
# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    # Convert the dictionary to a pandas DataFrame
    df = pd.DataFrame(list(data_dict.items()), columns=['Feature', 'Value'])
    
    # Initialize the MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df[['Value']])
    
    # Add the scaled values to the DataFrame
    df['Scaled Value'] = scaled_data[:, 0]
    
    # Plot the scaled data
    fig, ax = plt.subplots()
    ax.plot(df['Value'], label='Original Values')
    ax.plot(df['Scaled Value'], label='Scaled Values', color='orange')
    ax.set_title(PLOT_TITLE)
    ax.legend()
    
    return df, ax