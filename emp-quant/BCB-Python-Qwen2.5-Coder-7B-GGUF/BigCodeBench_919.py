
import pandas as pd
import matplotlib.pyplot as plt

def task_func(data, column):
    CATEGORIES = ['A', 'B', 'C', 'D', 'E']
    
    # Create a copy of the data to avoid modifying the original DataFrame
    data_copy = data.copy()
    
    # Replace missing values with 0 for the specified column
    data_copy[column] = data_copy[column].fillna(0)
    
    # Convert the column to categorical and reorder it based on CATEGORIES
    data_copy[column] = pd.Categorical(data_copy[column], categories=CATEGORIES, ordered=True)
    
    # Count the occurrences of each category
    category_counts = data_copy[column].value_counts()
    
    # Create a bar chart
    ax = category_counts.plot(kind='bar')
    
    # Set labels and title
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    # Show the plot
    plt.show()
    
    # Return the Axes object
    return ax