
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column):
    # Define the categories
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    
    # Ensure all categories are present in the data, with a count of zero if missing
    for category in CATEGORIES:
        if category not in data[column].values:
            data[column] = data[column].append(pd.Series({column: category, 'count': 0}), ignore_index=True)
    
    # Group the data by the specified column and sum the counts
    grouped_data = data.groupby(column).sum().reset_index()
    
    # Create the bar chart
    fig, ax = plt.subplots()
    ax.bar(grouped_data[column], grouped_data['count'], color='blue')
    
    # Set the labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    return ax