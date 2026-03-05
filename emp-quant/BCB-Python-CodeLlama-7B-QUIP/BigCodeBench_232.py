
import pandas as pd
import collections

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Get unique customer names
    unique_customers = df['Customer Name'].unique()

    # Get total sales
    total_sales = df['Sales'].sum()

    # Get most popular category
    category_counts = df['Category'].value_counts()
    most_popular_category = category_counts.index[0]

    return {
        'Total Sales': total_sales,
        'Most Popular Category': most_popular_category
    }

result = task_func(df)
print(result)