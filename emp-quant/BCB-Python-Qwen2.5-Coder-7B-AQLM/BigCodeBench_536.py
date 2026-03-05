
import sqlite3
import pandas as pd
import os

def task_func(db_name, table_name, csv_path="data.csv"):
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    
    # Read the table into a pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    # Close the database connection
    conn.close()
    
    # Ensure the directory for the CSV file exists
    csv_dir = os.path.dirname(csv_path)
    if not os.path.exists(csv_dir):
        os.makedirs(csv_dir)
    
    # Export the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)
    
    # Return the absolute path of the exported CSV file
    return os.path.abspath(csv_path)