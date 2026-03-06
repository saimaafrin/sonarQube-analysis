
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column):
    # Define the categories
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    
    # Ensure all categories are present in the data, filling missing counts with 0
    category_counts = data[column].value_counts().reindex(CATEGORIES, fill_value=0)
    
    # Create a bar chart
    ax = category_counts.plot(kind='bar')
    
    # Set labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    # Return the Axes object
    return ax