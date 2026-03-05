import pandas as pd
import seaborn as sns
from scipy import stats
def task_func(data):
    """
    Processes a given dataset to compute the average of each row, plots the distribution of these averages, and evaluates their normality.
    The function returns these averages as an additional column in a DataFrame, the plot of the distribution, and the p-value from the normality test if applicable.
    """
    # Check if the input data has exactly eight columns
    if len(data.columns) != 8:
        raise ValueError("The input data does not have exactly eight columns.")

    # Compute the average of each row
    averages = data.mean(axis=1)

    # Create a new DataFrame with the original data and the average column
    data_with_averages = pd.concat([data, pd.DataFrame(averages, columns=['Average'])], axis=1)

    # Plot the distribution of the averages
    sns.distplot(data_with_averages['Average'], kde=False, rug=True)
    ax = sns.plt.gca()

    # Evaluate the normality of the averages
    if len(data_with_averages['Average']) >= 20:
        p_value = stats.normaltest(data_with_averages['Average'])[1]
    else:
        p_value = None

    # Return the results
    return data_with_averages, ax, p_value
data = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [6, 7, 8, 9, 10], 'C': [11, 12, 13, 14, 15], 'D': [16, 17, 18, 19, 20], 'E': [21, 22, 23, 24, 25], 'F': [26, 27, 28, 29, 30], 'G': [31, 32, 33, 34, 35], 'H': [36, 37, 38, 39, 40]})