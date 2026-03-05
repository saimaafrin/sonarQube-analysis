import sqlite3
import pandas as pd
import seaborn as sns
def task_func(db_name="test.db", table_name="People"):
    # Connect to the database
    conn = sqlite3.connect(db_name)

    # Query the table
    query = f"SELECT age FROM {table_name}"
    df = pd.read_sql(query, conn)

    # Check for negative age values
    if df["age"].min() < 0:
        raise ValueError("Negative age values found in the data")

    # Create the plot
    sns.distplot(df["age"], bins=30, kde=True)

    # Return the Axes object
    return sns.axes._axes.Axes