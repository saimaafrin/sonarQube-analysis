import sqlite3
import pandas as pd
import os
def task_func(db_name, table_name, csv_path="data.csv"):
    # Connect to the database
    conn = sqlite3.connect(db_name)
    # Read the table into a pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    # Export the DataFrame to a CSV file
    df.to_csv(csv_path, index=False)
    # Close the database connection
    conn.close()
    # Return the absolute path of the exported CSV file
    return os.path.abspath(csv_path)
db_name = "example.db"
table_name = "example_table"
csv_path = "data.csv"