import pandas as pd
import sqlite3
def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    
    # Load data from the specified table into a DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)
    
    # Replace all occurrences of '\n' with '<br>' in the specified column
    df[column_name] = df[column_name].str.replace('\n', '<br>')
    
    # Close the database connection
    conn.close()
    
    # Return the modified DataFrame
    return df