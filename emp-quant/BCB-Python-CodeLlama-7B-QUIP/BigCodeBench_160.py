
import pandas as pd
import seaborn as sns
from scipy import stats
# Constants
COLUMN_NAMES = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
def task_func(data):
    # Check if the input data has exactly 8 columns
    if len(data.columns) != 8:
        raise ValueError("The input data must have exactly 8 columns")
    # Compute the average of each row
    averages = data.mean(axis=1)
    # Create a new DataFrame with the original data and the averages
    new_data = pd.concat([data, pd.DataFrame(averages, columns=['Average'])], axis=1)
    # Plot the distribution of the averages
    fig, ax = sns.distplot(new_data['Average'])
    # Perform the normality test
    if len(new_data['Average']) >= 20:
        p_value = stats.normaltest(new_data['Average'])
    else:
        p_value = None
    return new_data, ax, p_value