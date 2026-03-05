import pandas as pd
import collections
def task_func(df):
    """
    Generate a sales report from a DataFrame, excluding duplicate customer names.
    The report includes total sales and the most popular sales category.
    Note that:
    - The function will raise a ValueError if input df is not a DataFrame.
    - The function will return the first category in alphabetical order for "Most Popular Category" in the case of tie.
    - The function should output with:
        dict: A dictionary with keys 'Total Sales' (sum of sales) and 'Most Popular Category' (most frequent category).
    """
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input df must be a DataFrame.")

    # Calculate total sales
    total_sales = df["Sales"].sum()

    # Calculate most popular category
    category_counts = collections.Counter(df["Category"])
    most_popular_category = category_counts.most_common(1)[0][0]

    # Create report dictionary
    report = {
        "Total Sales": total_sales,
        "Most Popular Category": most_popular_category,
    }

    return report
df = pd.DataFrame({
    "Customer": ["Alice", "Bob", "Charlie", "Alice", "Bob"],
    "Sales": [100, 200, 300, 400, 500],
    "Category": ["Food", "Food", "Food", "Drinks", "Drinks"],
})