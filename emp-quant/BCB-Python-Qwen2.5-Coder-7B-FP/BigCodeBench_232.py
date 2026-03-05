import pandas as pd
import collections
def task_func(df):
    # Check if the input is a DataFrame
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")
    
    # Remove duplicate customer names
    df = df.drop_duplicates(subset='Customer Name')
    
    # Calculate total sales
    total_sales = df['Sales'].sum()
    
    # Find the most popular category
    category_counts = df['Category'].value_counts()
    most_popular_category = category_counts.idxmax()
    
    # In case of a tie, get the first category in alphabetical order
    if category_counts[most_popular_category] > 1:
        most_popular_category = sorted(category_counts[category_counts == category_counts[most_popular_category]].index)[0]
    
    # Return the result as a dictionary
    return {
        'Total Sales': total_sales,
        'Most Popular Category': most_popular_category
    }