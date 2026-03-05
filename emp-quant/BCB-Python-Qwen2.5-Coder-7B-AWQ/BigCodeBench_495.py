import pandas as pd
import numpy as np
def task_func(days, random_seed=0):
    """
    Generates a spending report DataFrame for the given number of days.

    Parameters:
    days (int): The number of days to generate data for.
    random_seed (int): The seed for the random number generator for reproducibility.

    Returns:
    pd.DataFrame: A DataFrame containing spending details for specified days, with shape (num_days, 5).
    """
    # Set the random seed for reproducibility
    np.random.seed(random_seed)

    # Create a date range starting from '2023-01-01' for the specified number of days
    date_range = pd.date_range(start='2023-01-01', periods=days)

    # Define the columns for the DataFrame
    columns = ['Groceries', 'Entertainment', 'Rent', 'Utilities', 'Miscellaneous']

    # Generate random spending data for each category
    spending_data = {
        column: np.random.randint(0, 101, size=days) for column in columns
    }

    # Create the DataFrame with the date range as the index and the spending data as the columns
    spending_report = pd.DataFrame(spending_data, index=date_range)

    return spending_report