from scipy import stats
import matplotlib.pyplot as plt
def task_func(data_dict, data_keys):
    """
    Calculate the correlation between two data series and return a scatter plot along with the correlation coefficient.
    """
    # Extract the data series from the dictionary
    x = data_dict[data_keys[0]]
    y = data_dict[data_keys[1]]

    # Calculate the correlation coefficient
    r, p = stats.pearsonr(x, y)

    # Create a scatter plot of the data series
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f"Correlation Coefficient: {r:.2f}")

    # Return the correlation coefficient and the scatter plot
    return r, ax
data_dict = {
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 6, 8, 10]
}
data_keys = ["x", "y"]