
import pandas as pd
import collections

def task_func(df):
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a DataFrame")

    # Calculate total sales
    total_sales = df["Sales"].sum()

    # Calculate most popular category
    category_counts = collections.Counter(df["Category"])
    most_popular_category = category_counts.most_common(1)[0][0]

    # Create output dictionary
    output = {
        "Total Sales": total_sales,
        "Most Popular Category": most_popular_category
    }

    return output