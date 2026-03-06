
import pandas as pd
import seaborn as sns
from scipy import stats

# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']

def task_func(data):
    # Check if the input data has exactly eight columns
    if len(data.columns) != 8:
        raise ValueError("Input data must have exactly eight columns")

    # Compute the average of each row
    averages = data.mean(axis=1)

    # Create a new DataFrame with the original data and the average column
    data_with_averages = pd.concat([data, pd.DataFrame(averages, columns=['Average'])], axis=1)

    # Plot the distribution of the averages
    ax = sns.distplot(data_with_averages['Average'])

    # Perform the normality test on the averages
    p_value = None
    if len(data_with_averages) >= 20:
        p_value = stats.normaltest(data_with_averages['Average'])[1]

    # Return the results
    return data_with_averages, ax, p_value