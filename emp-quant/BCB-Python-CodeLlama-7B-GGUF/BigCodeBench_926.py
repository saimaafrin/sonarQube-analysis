
import pandas as pd
import sqlite3

def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Query the table and convert to a Pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    # Replace newline characters with HTML line breaks
    df[column_name] = df[column_name].str.replace('\n', '<br>')

    # Close the SQLite connection
    conn.close()

    return df