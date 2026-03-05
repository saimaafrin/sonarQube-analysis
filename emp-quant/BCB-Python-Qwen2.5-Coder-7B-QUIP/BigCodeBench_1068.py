
import warnings
import sqlite3
import pandas as pd

def task_func(db_path, query, warn_large_dataset=True):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        # Execute the SQL query
        df = pd.read_sql_query(query, conn)
        # Close the database connection
        conn.close()

        # Check if the number of rows exceeds 10000
        if warn_large_dataset and len(df) > 10000:
            warnings.warn("The data contains more than 10000 rows.")

        return df
    except Exception as e:
        raise Exception(f"Error fetching data from the database: {e}")