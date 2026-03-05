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
    
    # Check if there are at least two numerical columns excluding 'id'
    numerical_columns = df.select_dtypes(include=[float, int]).columns
    if len(numerical_columns) < 2:
        raise ValueError("The table has less than two numerical columns.")
    
    # Exclude 'id' column if present
    if 'id' in numerical_columns:
        numerical_columns = numerical_columns.drop('id')
    
    # Plot the relationship between the first and second numerical columns
    fig, ax = plt.subplots()
    ax.scatter(df[numerical_columns[0]], df[numerical_columns[1]])
    
    # Label the axes with column names
    ax.set_xlabel(numerical_columns[0])
    ax.set_ylabel(numerical_columns[1])
    
    return ax