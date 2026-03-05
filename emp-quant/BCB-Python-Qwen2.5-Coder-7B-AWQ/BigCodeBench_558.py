import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
def task_func(a, b, columns=['A', 'B']):
    """
    Standardize two lists of numbers using the StandardScaler from sklearn and visualize the standardized values using a bar plot.
    
    Parameters:
    a (list): The first list of numbers.
    b (list): The second list of numbers.
    columns (list): The column names for the DataFrame.
    
    Returns:
    pd.DataFrame: A DataFrame containing the standardized values.
    matplotlib.axes.Axes: Axes object of the displayed bar plot.
    """
    # Combine the lists into a single array
    data = np.array([a, b]).T
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(data)
    
    # Create a DataFrame with the standardized data
    df = pd.DataFrame(standardized_data, columns=columns)
    
    # Create a bar plot of the standardized values
    ax = df.plot(kind='bar', figsize=(10, 6))
    
    # Set the title and labels
    ax.set_title('Standardized Values')
    ax.set_xlabel('Values')
    ax.set_ylabel('Standardized Values')
    
    return df, ax
a = [1, 2, 3, 4, 5]
b = [5, 4, 3, 2, 1]