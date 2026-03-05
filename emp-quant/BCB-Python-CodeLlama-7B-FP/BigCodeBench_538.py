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
    # Exclude the 'id' column
    df = df.drop(columns=['id'])
    # Check if the table has less than two numerical columns
    if len(df.select_dtypes(include=[np.number]).columns) < 2:
        raise ValueError("ValueError: If the table has less than two numerical columns.")
    # Plot the relationship
    fig, ax = plt.subplots()
    ax.scatter(df.iloc[:, 0], df.iloc[:, 1])
    ax.set_xlabel(df.columns[0])
    ax.set_ylabel(df.columns[1])
    plt.show()
    return fig
db_name = "example.db"
table_name = "example_table"