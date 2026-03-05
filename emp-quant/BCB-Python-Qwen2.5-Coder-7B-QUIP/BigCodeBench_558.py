
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(a, b, columns=['A', 'B']):
    # Combine the lists into a single DataFrame
    data = pd.DataFrame({'A': a, 'B': b})
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(data)
    
    # Create a DataFrame with the scaled values
    scaled_df = pd.DataFrame(scaled_data, columns=columns)
    
    # Create a bar plot for the scaled values
    fig, ax = plt.subplots()
    scaled_df.plot(kind='bar', ax=ax)
    
    # Set the plot title and labels
    ax.set_title('Standardized Values')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Standardized Values')
    
    # Return the DataFrame and the Axes object
    return scaled_df, ax