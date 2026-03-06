
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    """
    Generates a category distribution within a specified range and returns as a DataFrame.

    Parameters:
    value_range (tuple): A tuple containing the start and end values for the range.

    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Category' and 'Count'.
    """
    # Generate random data points within the specified range
    data_points = [random.randint(*value_range) for _ in range(1000)]
    
    # Count occurrences of each category based on the generated data points
    category_counts = {}
    for point in data_points:
        if point % len(CATEGORIES) == 0:
            category = CATEGORIES[0]
        else:
            category = CATEGORIES[point % len(CATEGORIES)]
        category_counts[category] = category_counts.get(category, 0) + 1
    
    # Create a DataFrame from the category counts
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df