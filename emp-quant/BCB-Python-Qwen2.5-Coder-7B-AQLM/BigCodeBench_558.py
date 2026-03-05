
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def task_func(a, b, columns=['A', 'B']):
    # Combine the lists into a single array
    data = np.vstack((a, b))
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(data)
    
    # Create a DataFrame with the standardized data
    standardized_df = pd.DataFrame(standardized_data, columns=columns)
    
    # Create a bar plot of the standardized values
    ax = standardized_df.plot(kind='bar', figsize=(10, 6))
    
    # Set the title and labels
    ax.set_title('Standardized Values')
    ax.set_xlabel('Columns')
    ax.set_ylabel('Standardized Values')
    
    # Return the DataFrame and the Axes object
    return standardized_df, ax