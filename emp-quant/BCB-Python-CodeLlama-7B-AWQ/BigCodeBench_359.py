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
    # Check if the input is valid
    if not isinstance(data_dict, dict) or not isinstance(data_keys, list):
        raise ValueError("Invalid input type")
    if len(data_keys) != 2:
        raise ValueError("Expected two data keys")

    # Extract the data series
    x = data_dict[data_keys[0]]
    y = data_dict[data_keys[1]]

    # Calculate the correlation coefficient
    r, _ = stats.pearsonr(x, y)

    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(x, y)
    ax.set_xlabel(data_keys[0])
    ax.set_ylabel(data_keys[1])
    ax.set_title(f"Correlation Coefficient: {r:.2f}")

    return r, ax
data_dict = {
    "x": [1, 2, 3, 4, 5],
    "y": [2, 4, 6, 8, 10]
}
data_keys = ["x", "y"]