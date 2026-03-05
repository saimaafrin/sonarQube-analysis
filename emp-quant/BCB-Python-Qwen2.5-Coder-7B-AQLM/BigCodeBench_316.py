
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    """
    Generates a category distribution within a specified range and returns as a DataFrame.
    
    Parameters:
    value_range (tuple): A tuple containing the minimum and maximum values for the range.
    
    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Category' and 'Count'.
    """
    # Generate random values within the specified range
    values = [random.randint(value_range[0], value_range[1]) for _ in range(1000)]
    
    # Count occurrences of each category
    category_counts = {}
    for value in values:
        category = CATEGORIES[value % len(CATEGORIES)]
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    # Create DataFrame
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df