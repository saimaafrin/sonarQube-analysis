
from scipy import stats
import matplotlib.pyplot as plt

def task_func(data_dict, data_keys):
    # Extract the data series from the dictionary using the provided keys
    data1 = data_dict[data_keys[0]]
    data2 = data_dict[data_keys[1]]
    
    # Calculate the correlation coefficient
    correlation_coefficient = stats.pearsonr(data1, data2)[0]
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data1, data2)
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f'Scatter Plot of {data_keys[0]} vs {data_keys[1]}')
    
    # Return the correlation coefficient and the scatter plot
    return correlation_coefficient, ax