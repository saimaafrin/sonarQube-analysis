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
    
    # Determine the category for each value
    categories = [CATEGORIES[value % len(CATEGORIES)] for value in values]
    
    # Create a DataFrame with category counts
    category_counts = pd.DataFrame(categories, columns=['Category'])
    category_counts['Count'] = category_counts['Category'].value_counts()
    
    return category_counts