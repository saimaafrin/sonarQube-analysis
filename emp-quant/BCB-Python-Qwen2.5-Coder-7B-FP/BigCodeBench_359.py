from scipy import stats
import matplotlib.pyplot as plt
def task_func(data_dict, data_keys):
    """
    Calculate the correlation between two data series and return a scatter plot along with the correlation coefficient.
    
    Parameters:
    data_dict (dict): A dictionary containing the data series.
    data_keys (list): A list of two keys corresponding to the data series to be analyzed.
    
    Returns:
    tuple: A tuple containing the correlation coefficient and the Axes object of the scatter plot.
    """
    # Extract the data series from the dictionary
    data1 = data_dict[data_keys[0]]
    data2 = data_dict[data_keys[1]]
    
    # Calculate the correlation coefficient
    correlation_coefficient, _ = stats.pearsonr(data1, data2)
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(data1, data2)
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f'Scatter Plot of {data_keys[0]} vs {data_keys[1]}')
    
    return correlation_coefficient, ax
data_dict = {
    'temperature': [22, 24, 19, 23, 25, 21, 20],
    'sales': [150, 180, 120, 160, 200, 170, 140]
}
data_keys = ['temperature', 'sales']