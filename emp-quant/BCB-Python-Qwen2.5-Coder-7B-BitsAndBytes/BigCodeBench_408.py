
import sqlite3
import pandas as pd

def task_func(db_file: str, query: str) -> pd.DataFrame:
    """
    Connects to a given SQLite database, executes a given SQL query,
    and returns the results as a pandas DataFrame.

    Parameters:
    db_file (str): The path to the SQLite database file.
    query (str): The SQL query to execute.

    Returns:
    pd.DataFrame: A DataFrame containing the results of the executed query.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    # Execute the query and fetch the results
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    return df