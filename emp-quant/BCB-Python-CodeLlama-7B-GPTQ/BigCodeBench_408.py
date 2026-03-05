import sqlite3
import pandas as pd
def task_func(db_file: str, query: str) -> pd.DataFrame:
    """
    Query an SQLite database and return the results.

    Args:
        db_file (str): Path to the SQLite database file.
        query (str): SQL query to execute.

    Returns:
        pd.DataFrame: A DataFrame containing the results of the executed query.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Convert the results to a pandas DataFrame
    df = pd.DataFrame(results)

    # Close the connection
    conn.close()

    return df
db_file = "example.db"
query = "SELECT * FROM example_table"