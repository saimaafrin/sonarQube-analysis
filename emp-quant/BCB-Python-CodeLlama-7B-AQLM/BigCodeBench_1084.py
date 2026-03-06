import pandas as pd
from sklearn.feature_selection import f_oneway
def task_func(data_file_path: str):
    """
    Analyzes numerical data from a CSV file. The function reads the CSV file, converts string representations of
    numbers with commas into floating point numbers, calculates the mean and standard deviation for each numerical column,
    generates a histogram plot for each numerical column, and performs an ANOVA test to check the statistical significance 
    of differences between means of numerical columns (if applicable).

    Parameters:
    - data_file_path (str): Path to the CSV data file.

    Returns:
    - means (pd.Series): Mean values of each numerical column.
    - std_devs (pd.Series): Standard deviation values of each numerical column.
    - axes (list[matplotlib.axes.Axes]): List of histogram plots for each numerical column.
    - anova_results (pd.DataFrame): ANOVA test results for each pair of numerical columns (if more than one numerical column is present).

    Requirements:
    - pandas
    - sklearn

    Note:
    - The function assumes that all columns in the CSV file contain numerical data or string representations of numerical data.
    - The ANOVA test is only performed if there are two or more numerical columns. Compute two columns "F-value" and "P-value" for each pair of numerical columns.

    Example:
    >>> means, std_devs, axes, anova_results = task_func('data.csv')
    >>> print(f'Means: {means}, Standard Deviations: {std_devs}')
    >>> print(anova_results)
    """
    # Read the CSV file
    df = pd.read_csv(data_file_path)

    # Convert string representations of numbers with commas into floating point numbers
    df = df.apply(lambda x: pd.to_numeric(x, errors='coerce'))

    # Calculate the mean and standard deviation for each numerical column
    means = df.select_dtypes(include=['number']).mean()
    std_devs = df.select_dtypes(include=['number']).std()

    # Generate a histogram plot for each numerical column
    axes = []
    for col in df.select_dtypes(include=['number']).columns:
        axes.append(df[col].hist(bins=100))

    # Perform an ANOVA test to check the statistical significance of differences between means of numerical columns
    anova_results = None
    if len(df.select_dtypes(include=['number']).columns) > 1:
        anova_results = pd.DataFrame(f_oneway(df.select_dtypes(include=['number']).columns))
        anova_results.columns = ['F-value', 'P-value']

    return means, std_devs, axes, anova_results