
import sqlite3
import pandas as pd

def task_func(db_file: str, query: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    # Execute the query
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    # Return the DataFrame
    return df