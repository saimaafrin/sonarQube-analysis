
import sqlite3
import pandas as pd
import os

def task_func(db_file, table_name, column_name, pattern='\d+[xX]'):
    # Check if the database file exists
    if not os.path.exists(db_file):
        raise ValueError("The database file does not exist.")
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    # Query to select all entries from the specified table
    query = f"SELECT * FROM {table_name}"
    
    # Load the data into a pandas DataFrame
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Filter the DataFrame to find matches with the regex pattern
    matches = df[df[column_name].str.contains(pattern, na=False)]
    
    # Return the DataFrame with matches
    return matches