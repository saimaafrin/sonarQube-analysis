import pandas as pd
import matplotlib.pyplot as plt
def task_func(data, column):
    # Define the categories
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    
    # Create a DataFrame from the input data
    df = pd.DataFrame(data)
    
    # Get the counts of each category in the specified column
    category_counts = df[column].value_counts().reindex(CATEGORIES, fill_value=0)
    
    # Create a bar chart
    ax = category_counts.plot(kind='bar')
    
    # Set the labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    # Return the Axes object
    return ax