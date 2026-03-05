import pandas as pd
import random
CATEGORIES = ['A', 'B', 'C', 'D', 'E']
def task_func(value_range=(0, 100)):
    """
    Generate a category distribution within a specified range and return as a DataFrame.
    """
    # Generate random values within the specified range
    values = [random.randint(value_range[0], value_range[1]) for _ in range(len(CATEGORIES))]

    # Create a DataFrame with two columns: 'Category' and 'Count'
    df = pd.DataFrame({'Category': CATEGORIES, 'Count': values})

    # Sort the DataFrame by 'Count' in descending order
    df.sort_values(by='Count', ascending=False, inplace=True)

    return df