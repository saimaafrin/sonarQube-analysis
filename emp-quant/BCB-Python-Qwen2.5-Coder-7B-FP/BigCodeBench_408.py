import sqlite3
import pandas as pd
def task_func(db_file: str, query: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    # Execute the SQL query
    df = pd.read_sql_query(query, conn)
    
    # Close the database connection
    conn.close()
    
    # Return the results as a pandas DataFrame
    return df