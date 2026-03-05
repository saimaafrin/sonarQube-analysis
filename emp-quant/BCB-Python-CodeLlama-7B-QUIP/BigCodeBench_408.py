
import sqlite3
import pandas as pd

def task_func(db_file: str, query: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)

    # Execute the SQL query
    with conn:
        cursor = conn.cursor()
        cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Convert the results to a DataFrame
    df = pd.DataFrame(results, columns=cursor.description[0])

    return df