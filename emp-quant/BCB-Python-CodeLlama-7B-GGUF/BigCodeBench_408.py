
import sqlite3
import pandas as pd

def task_func(db_file: str, query: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch the results as a pandas DataFrame
    df = pd.DataFrame(cursor.fetchall())

    # Close the connection
    conn.close()

    return df