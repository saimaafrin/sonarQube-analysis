
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def task_func(db_name, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Query the table into a pandas DataFrame
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Check if there are at least two numerical columns
    if df.select_dtypes(include=['number']).shape[1] < 2:
        raise ValueError("The table has less than two numerical columns.")
    
    # Get the names of the numerical columns
    numerical_columns = df.select_dtypes(include=['number']).columns
    
    # Create a scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[numerical_columns[0]], df[numerical_columns[1]])
    
    # Set the labels for the axes
    ax.set_xlabel(numerical_columns[0])
    ax.set_ylabel(numerical_columns[1])
    
    # Return the axes object
    return ax