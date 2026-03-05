
import sqlite3
import pandas as pd
import seaborn as sns

def task_func(db_name="test.db", table_name="People"):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    # Query the table
    query = "SELECT age FROM " + table_name
    df = pd.read_sql(query, conn)
    # Check for negative values
    if any(df['age'] < 0):
        raise ValueError("Negative age values in the data")
    # Plot the histogram
    fig, ax = sns.histplot(df['age'], bins=30, kde=True)
    return ax