
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

    # Create a new DataFrame with the original data and the average column
    df = pd.concat([data, pd.DataFrame(averages, columns=['Average'])], axis=1)

    # Plot the distribution of the averages
    ax = sns.distplot(df['Average'], bins=20)

    # Perform the normality test if there are at least 20 data points
    if len(df) >= 20:
        p_value = stats.normaltest(df['Average'])[1]
    else:
        p_value = None

    return df, ax, p_value