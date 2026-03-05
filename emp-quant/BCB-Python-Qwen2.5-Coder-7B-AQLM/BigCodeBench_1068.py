
import warnings
import sqlite3
import pandas as pd

def task_func(db_path, query, warn_large_dataset=True):
    try:
        # Connect to the SQLite database
        conn = sqlite3.connect(db_path)
        
        # Execute the SQL query
        df = pd.read_sql_query(query, conn)
        
        # Check if the dataset is large
        if warn_large_dataset and len(df) > 10000:
            warnings.warn("The data contains more than 10000 rows.")
        
        # Close the database connection
        conn.close()
        
        return df
    
    except Exception as e:
        # Raise an exception with a custom error message
        raise Exception(f"Error fetching data from the database: {str(e)}")