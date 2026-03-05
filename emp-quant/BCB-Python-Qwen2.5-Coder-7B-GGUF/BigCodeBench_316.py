
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    """
    Generates a category distribution within a specified range and returns as a DataFrame.
    
    Parameters:
    value_range (tuple): A tuple of two integers representing the range (min, max).
    
    Returns:
    DataFrame: A pandas DataFrame with two columns: 'Category' and 'Count'.
    """
    # Generate random data within the specified range
    data = [random.randint(value_range[0], value_range[1]) for _ in range(1000)]
    
    # Count occurrences of each category
    category_counts = {}
    for value in data:
        if value % 20 == 0:  # Assign category based on value
            category = CATEGORIES[value // 20]
        else:
            category = 'Other'
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    # Create DataFrame
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df