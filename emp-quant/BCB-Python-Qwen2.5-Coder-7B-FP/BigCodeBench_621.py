from itertools import chain
import numpy as np
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
def task_func(L):
    # Flatten the list of lists into a single list
    flattened_list = list(chain.from_iterable(L))
    
    # Convert the list of integers to a numpy array
    data_array = np.array(flattened_list)
    
    # Standardize the data
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_array.reshape(-1, 1))
    
    # Plot the standardized values
    plt.figure(figsize=(10, 6))
    plt.plot(standardized_data, marker='o', linestyle='-', color='b')
    plt.title('Standardized Values')
    plt.xlabel('Index')
    plt.ylabel('Standardized Value')
    plt.grid(True)
    plt.show()
    
    return plt.gca()  # Return the current Axes instance on the current figure