
import pandas as pd
import collections

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Remove duplicates based on customer name
    df = df.drop_duplicates(subset='Customer Name')
    
    # Calculate total sales
    total_sales = df['Sales'].sum()
    
    # Find the most popular category
    category_counts = df['Category'].value_counts()
    most_popular_category = category_counts.idxmax()
    
    # In case of tie, get the first category in alphabetical order
    if category_counts[most_popular_category] > 1:
        sorted_categories = category_counts[category_counts == category_counts[most_popular_category]].index.tolist()
        sorted_categories.sort()
        most_popular_category = sorted_categories[0]
    
    return {
        'Total Sales': total_sales,
        'Most Popular Category': most_popular_category
    }