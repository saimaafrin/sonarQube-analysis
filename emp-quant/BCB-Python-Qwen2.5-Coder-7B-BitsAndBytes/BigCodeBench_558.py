
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(a, b, columns=['A', 'B']):
    # Combine the input arrays into a single array
    data = np.vstack((a, b))
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    scaled_data = scaler.fit_transform(data)
    
    # Create a DataFrame with the scaled data
    df_scaled = pd.DataFrame(scaled_data, columns=columns)
    
    # Plotting the bar plot
    fig, ax = plt.subplots()
    df_scaled.plot(kind='bar', ax=ax)
    ax.set_title('Bar Plot of Standardized Values')
    ax.set_xlabel('Data Index')
    ax.set_ylabel('Standardized Value')
    
    return df_scaled, ax