
import pandas as pd
import random

# Constants
CATEGORIES = ['A', 'B', 'C', 'D', 'E']

def task_func(value_range=(0, 100)):
    # Generate a list of random values within the specified range
    values = [random.randint(value_range[0], value_range[1]) for _ in range(1000)]
    
    # Count the occurrences of each category
    category_counts = {}
    for value in values:
        category = CATEGORIES[value % len(CATEGORIES)]
        if category not in category_counts:
            category_counts[category] = 0
        category_counts[category] += 1
    
    # Create a DataFrame from the category counts
    df = pd.DataFrame(list(category_counts.items()), columns=['Category', 'Count'])
    
    return df