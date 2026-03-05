from scipy import stats
import matplotlib.pyplot as plt
def task_func(data_dict, data_keys):
    """
    Calculate the correlation between two data series and return a scatter plot along with the correlation coefficient.

    Args:
        data_dict (dict): A dictionary containing the data series.
        data_keys (list): A list of keys corresponding to the data series.

    Returns:
        tuple:
            float: The correlation coefficient.
            Axes: The scatter plot of the two data series.
    """
    # Extract the data series from the dictionary
    data1 = data_dict[data_keys[0]]
    data2 = data_dict[data_keys[1]]

    # Calculate the correlation coefficient
    correlation_coefficient = stats.pearsonr(data1, data2)[0]

    # Create a scatter plot of the two data series
    fig, ax = plt.subplots()
    ax.scatter(data1, data2)
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f"Correlation Coefficient: {correlation_coefficient}")

    return correlation_coefficient, ax
data_dict = {
    "data1": [1, 2, 3, 4, 5],
    "data2": [2, 4, 6, 8, 10],
}
data_keys = ["data1", "data2"]