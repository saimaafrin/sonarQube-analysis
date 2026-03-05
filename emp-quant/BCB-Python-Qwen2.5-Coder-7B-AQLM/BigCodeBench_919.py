
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column):
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    
    # Ensure all categories are present in the data, with count 0 if missing
    data[column] = data[column].astype(str)
    category_counts = data[column].value_counts().reindex(CATEGORIES, fill_value=0)
    
    # Create the bar chart
    ax = category_counts.plot(kind='bar', figsize=(10, 6))
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    return ax