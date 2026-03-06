import pandas as pd
import collections
def task_func(df):
    """
    Generate a sales report from a DataFrame, excluding duplicate customer names. 
    The report includes total sales and the most popular sales category.

    Parameters:
    df (DataFrame): A pandas DataFrame with columns 'Customer', 'Category', and 'Sales'.

    Returns:
    dict: A dictionary with keys 'Total Sales' (sum of sales) and 'Most Popular Category' (most frequent category).

    Requirements:
    - pandas
    - collections

    Raises:
    - The function will raise a ValueError is input df is not a DataFrame.

    Note:
    - The function would return the first category in alphabetical order for "Most Popular Category' in the case of tie

    Example:
    >>> data = pd.DataFrame([{'Customer': 'John', 'Category': 'Electronics', 'Sales': 500}, {'Customer': 'Mary', 'Category': 'Home', 'Sales': 300}])
    >>> report = task_func(data)
    >>> print(report)
    {'Total Sales': 800, 'Most Popular Category': 'Electronics'}
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError('Input df is not a DataFrame')

    # Create a new DataFrame with unique customer names
    df_unique = df.drop_duplicates(subset=['Customer'])

    # Create a new DataFrame with customer names and total sales
    df_total = df_unique.groupby('Customer').sum()

    # Create a new DataFrame with customer names and most popular category
    df_category = df_unique.groupby('Customer').Category.value_counts().reset_index()
    df_category.columns = ['Customer', 'Category']
    df_category = df_category.sort_values(by='Category', ascending=False)
    df_category = df_category.groupby('Customer').first()

    # Merge the two DataFrames
    df_merged = pd.merge(df_total, df_category, on='Customer')

    # Create a dictionary with the report
    report = {'Total Sales': df_merged['Sales'].sum(), 'Most Popular Category': df_merged['Category'].iloc[0]}

    return report