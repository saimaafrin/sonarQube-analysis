
import sqlite3
import pandas as pd
import os

def task_func(db_name, table_name, csv_path="data.csv"):
    # Connect to the SQLite3 database
    conn = sqlite3.connect(db_name)
    # Create a pandas DataFrame from the table
    df = pd.read_sql_table(table_name, conn)
    # Export the DataFrame to a CSV file
    df.to_csv(csv_path)
    # Return the absolute path of the exported CSV file
    return os.path.abspath(csv_path)