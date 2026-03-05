
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def task_func(db_name, table_name):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    # Get the table
    table = pd.read_sql_table(table_name, conn)
    # Check if the table has less than two numerical columns
    if len(table.columns) < 2:
        raise ValueError("Table must have at least two numerical columns")
    # Get the first and second numerical columns
    x = table.iloc[:, 1]
    y = table.iloc[:, 2]
    # Plot the relationship
    plt.scatter(x, y)
    plt.xlabel(x.name)
    plt.ylabel(y.name)
    plt.show()
    return plt