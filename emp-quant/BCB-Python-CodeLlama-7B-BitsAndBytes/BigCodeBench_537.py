
import sqlite3
import pandas as pd
import seaborn as sns

def task_func(db_name="test.db", table_name="People"):
    # Connect to the database
    conn = sqlite3.connect(db_name)

    # Query the table to get the age data
    query = "SELECT age FROM {}".format(table_name)
    df = pd.read_sql_query(query, conn)

    # Check for negative age values
    if df['age'].min() < 0:
        raise ValueError("Negative age values found in the data")

    # Create the age distribution plot
    ax = sns.distplot(df['age'], bins=30, kde=True)

    # Close the connection to the database
    conn.close()

    return ax