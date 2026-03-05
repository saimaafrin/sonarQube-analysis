
import pandas as pd
import collections

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame")
    
    # Remove duplicate customer names
    df = df.drop_duplicates(subset='customer_name')
    
    # Calculate total sales
    total_sales = df['sales'].sum()
    
    # Get the most popular category
    category_counts = df['category'].value_counts()
    most_popular_category = category_counts.idxmax()
    
    # Return the results as a dictionary
    return {
        'Total Sales': total_sales,
        'Most Popular Category': most_popular_category
    }