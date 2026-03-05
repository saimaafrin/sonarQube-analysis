import pandas as pd
import matplotlib.pyplot as plt
CATEGORIES = ['A', 'B', 'C', 'D', 'E']
def task_func(data, column):
    # Create a DataFrame from the input data
    df = pd.DataFrame(data)
    
    # Count the occurrences of each category in the specified column
    category_counts = df[column].value_counts()
    
    # Create a new DataFrame with all categories, including those with zero counts
    all_categories = pd.DataFrame({column: pd.Categorical(df[column], categories=CATEGORIES)})
    category_counts = all_categories[column].value_counts().reindex(CATEGORIES, fill_value=0)
    
    # Plot the bar chart
    ax = category_counts.plot(kind='bar')
    ax.set_xlabel('Category')
    ax.set_ylabel('Count')
    ax.set_title(f'Distribution of {column}')
    
    return ax