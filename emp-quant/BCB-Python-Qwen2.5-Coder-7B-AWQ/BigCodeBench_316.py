import pandas as pd
import random
CATEGORIES = ['A', 'B', 'C', 'D', 'E']
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
        if value % 20 < 4:  # Assign category based on value
            category = CATEGORIES[0]
        elif value % 20 < 8:
            category = CATEGORIES[1]
        elif value % 20 < 12:
            category = CATEGORIES[2]
        elif value % 20 < 16:
            category = CATEGORIES[3]
        else:
            category = CATEGORIES[4]
        
        if category in category_counts:
            category_counts[category] += 1
        else:
            category_counts[category] = 1
    
    # Create DataFrame
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df