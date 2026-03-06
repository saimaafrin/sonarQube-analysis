
import sqlite3
import pandas as pd

def task_func(db_file: str, query: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # Execute the SQL query
    cursor = conn.cursor()
    cursor.execute(query)

    # Fetch the results of the query
    results = cursor.fetchall()

    # Convert the results to a Pandas DataFrame
    df = pd.DataFrame(results)

    # Close the connection to the database
    conn.close()

    return df