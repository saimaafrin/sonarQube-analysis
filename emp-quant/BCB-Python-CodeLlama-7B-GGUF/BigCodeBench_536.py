
import sqlite3
import pandas as pd
import os

def task_func(db_name, table_name, csv_path="data.csv"):
    # Connect to the SQLite3 database
    conn = sqlite3.connect(db_name)

    # Read the table from the database
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    # Export the data to a CSV file
    df.to_csv(csv_path, index=False)

    # Close the connection to the database
    conn.close()

    # Return the absolute path of the exported CSV file
    return os.path.abspath(csv_path)