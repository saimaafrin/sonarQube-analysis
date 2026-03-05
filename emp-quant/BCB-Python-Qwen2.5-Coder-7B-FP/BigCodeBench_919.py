import pandas as pd
import matplotlib.pyplot as plt
CATEGORIES = ['A', 'B', 'C', 'D', 'E']
def task_func(data, column):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data)
    
    # Count the occurrences of each category in the specified column
    category_counts = df[column].value_counts()
    
    # Reindex the counts to include all categories, filling missing values with 0
    category_counts = category_counts.reindex(CATEGORIES, fill_value=0)
    
    # Plot the bar chart
    ax = category_counts.plot(kind='bar')
    
    # Set the labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    # Return the Axes object
    return ax