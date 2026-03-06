import bisect
import statistics
def task_func(df, column, value):
    """
    Analyze a column of a pandas DataFrame, find the values that are larger than the average, and count the number of values that are larger than a given value.

    Parameters:
    df (DataFrame): The pandas DataFrame.
    column (str): The column to analyze.
    value (float): The value to compare with the data in the column.
    
    Returns:
    tuple: A tuple containing (numpy.ndarray, int, matplotlib.axes.Axes).
           The numpy array contains values greater than the average.
           The int is the number of values greater than the given value.
           The Axes object is for the generated histogram plot.

    Raises:
    ValueError: If the column does not exist in the DataFrame or value is not a number.

    Requirements:
    - bisect
    - statistics
    
    Example:
    >>> df = pd.DataFrame({'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]})
    >>> greater_avg, num_greater_value, ax = task_func(df, 'A', 5)
    """
    if column not in df.columns:
        raise ValueError('Column does not exist in the DataFrame.')
    if not isinstance(value, (int, float)):
        raise ValueError('Value is not a number.')

    # Get the average of the column.
    avg = df[column].mean()

    # Get the values greater than the average.
    greater_avg = df[df[column] > avg][column]

    # Get the number of values greater than the given value.
    num_greater_value = len(greater_avg[greater_avg > value])

    # Generate a histogram plot.
    ax = greater_avg.hist(bins=10, color='#0072B2', edgecolor='#0072B2', linewidth=1.5, density=True)

    return greater_avg, num_greater_value, ax