import pandas as pd
import random
def task_func(value_range=(0, 100)):
    """
    Generate a category distribution within a specified range and return as a DataFrame.
    
    Parameters:
    - value_range: A tuple (min, max) representing the range of values to generate.
    
    Returns:
    - A pandas DataFrame with two columns: 'Category' and 'Count'.
    """
    # Generate random values within the specified range
    values = [random.randint(value_range[0], value_range[1]) for _ in range(1000)]
    
    # Count occurrences of each category
    category_counts = {}
    for value in values:
        if value % 20 < 4:  # Assign categories based on value ranges
            category_counts['A'] = category_counts.get('A', 0) + 1
        elif value % 20 < 8:
            category_counts['B'] = category_counts.get('B', 0) + 1
        elif value % 20 < 12:
            category_counts['C'] = category_counts.get('C', 0) + 1
        elif value % 20 < 16:
            category_counts['D'] = category_counts.get('D', 0) + 1
        else:
            category_counts['E'] = category_counts.get('E', 0) + 1
    
    # Create DataFrame
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df