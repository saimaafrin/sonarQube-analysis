
import sqlite3
import pandas as pd
import seaborn as sns

def task_func(db_name="test.db", table_name="People"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Query the data from the table
    query = f"SELECT age FROM {table_name}"
    data = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Check for negative age values
    if data['age'].min() < 0:
        raise ValueError("Data contains negative age values")
    
    # Create a plot of the age distribution
    ax = sns.histplot(data['age'], bins=30, kde=True)
    
    # Set the x-axis label
    ax.set_xlabel('age')
    
    # Return the Axes object
    return ax