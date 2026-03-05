import pandas as pd
import seaborn as sns
def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    """
    Load a CSV file into a DataFrame, filter the lines in which the employee ID begins with a prefix, and draw a histogram of its age.

    Args:
        data (str): Path to the CSV file.
        emp_prefix (str): Prefix for the employee ID.

    Returns:
        DataFrame: A pandas DataFrame with the filtered data, containing the columns 'Employee ID' and 'Age'.
        Axes: A histogram plot of the 'Age' column of the filtered data.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(data)

    # Filter the DataFrame to include only rows where the employee ID begins with the specified prefix
    df = df[df['Employee ID'].str.startswith(emp_prefix)]

    # Draw a histogram of the 'Age' column of the filtered DataFrame
    sns.histplot(data=df, x='Age')

    # Return the filtered DataFrame and the histogram plot
    return df, sns.histplot(data=df, x='Age')
data = '/path/to/data.csv'
emp_prefix = 'EMP'