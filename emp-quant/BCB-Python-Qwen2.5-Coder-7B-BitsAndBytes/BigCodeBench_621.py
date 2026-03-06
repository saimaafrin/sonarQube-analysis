
from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

def task_func(L):
    # Flatten the list of lists into a single list
    flattened_list = list(chain.from_iterable(L))
    
    # Convert the list to a numpy array
    data_array = np.array(flattened_list)
    
    # Initialize the StandardScaler
    scaler = StandardScaler()
    
    # Fit and transform the data
    standardized_data = scaler.fit_transform(data_array.reshape(-1, 1)).flatten()
    
    # Plot the standardized values
    fig, ax = plt.subplots()
    ax.plot(standardized_data, marker='o')
    ax.set_title('Standardized Values')
    ax.set_xlabel('Index')
    ax.set_ylabel('Standardized Value')
    
    return ax