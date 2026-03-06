
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

def task_func(db_name, table_name):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Query the table into a DataFrame
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    # Check if there are at least two numerical columns (excluding 'id')
    numerical_columns = [col for col in df.columns if pd.api.types.is_numeric_dtype(df[col]) and col != 'id']
    
    if len(numerical_columns) < 2:
        raise ValueError("The table must have at least two numerical columns excluding 'id'.")
    
    # Plotting the scatter plot
    fig, ax = plt.subplots()
    ax.scatter(df[numerical_columns[0]], df[numerical_columns[1]])
    
    # Labeling the axes
    ax.set_xlabel(numerical_columns[0])
    ax.set_ylabel(numerical_columns[1])
    
    return ax