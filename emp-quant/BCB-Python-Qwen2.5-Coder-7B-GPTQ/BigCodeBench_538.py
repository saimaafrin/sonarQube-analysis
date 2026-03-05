import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
def task_func(db_name, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Query the table into a pandas DataFrame
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Check if there are at least two numerical columns
    numerical_columns = df.select_dtypes(include=[float, int]).columns
    if len(numerical_columns) < 2:
        raise ValueError("The table has less than two numerical columns.")
    
    # Get the first two numerical columns
    first_column = numerical_columns[0]
    second_column = numerical_columns[1]
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[first_column], df[second_column])
    
    # Label the axes
    ax.set_xlabel(first_column)
    ax.set_ylabel(second_column)
    
    # Return the axes object
    return ax