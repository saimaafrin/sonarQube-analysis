
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler

# Constants
PLOT_TITLE = "Scaled Values"

def task_func(data_dict):
    # Convert dictionary to DataFrame
    df = pd.DataFrame(list(data_dict.items()), columns=['Feature', 'Value'])
    
    # Initialize MinMaxScaler
    scaler = MinMaxScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(df[['Value']])
    
    # Add scaled data back to DataFrame
    df['Scaled_Value'] = scaled_data
    
    # Plotting
    fig, ax = plt.subplots()
    ax.plot(df['Feature'], df['Scaled_Value'], marker='o')
    ax.set_title(PLOT_TITLE)
    ax.set_xlabel('Feature')
    ax.set_ylabel('Scaled Value')
    
    return df, ax