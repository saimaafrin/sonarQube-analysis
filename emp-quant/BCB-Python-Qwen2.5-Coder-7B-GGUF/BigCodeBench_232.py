
import pandas as pd
import collections

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df is not a DataFrame.")
    
    # Remove duplicate customer names
    df = df.drop_duplicates(subset='Customer Name')
    
    # Calculate total sales
    total_sales = df['Sales'].sum()
    
    # Find the most popular category
    category_counts = collections.Counter(df['Category'])
    most_popular_category = category_counts.most_common(1)[0][0]
    
    # Handle tie by selecting the first category in alphabetical order
    if len(category_counts) > 1 and category_counts.most_common(2)[0][1] == category_counts.most_common(2)[1][1]:
        most_popular_category = min([category for category, count in category_counts.items() if count == category_counts.most_common(1)[0][1]])
    
    return {
        'Total Sales': total_sales,
        'Most Popular Category': most_popular_category
    }