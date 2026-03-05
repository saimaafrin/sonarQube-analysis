import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
def task_func(db_name, table_name):
    """
    Plot the relationship between the first and second numerical columns of an SQLite3 table, after excluding 'id' column.
    """
    # Connect to the database
    conn = sqlite3.connect(db_name)

    # Get the table
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    # Check if the table has less than two numerical columns
    if len(df.select_dtypes(include=[np.number]).columns) < 2:
        raise ValueError("ValueError: Table has less than two numerical columns.")

    # Get the first and second numerical columns
    x = df.iloc[:, 0]
    y = df.iloc[:, 1]

    # Plot the data
    plt.scatter(x, y)
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.title(f"{table_name} Scatterplot")
    plt.show()
db_name = "example.db"
table_name = "example_table"