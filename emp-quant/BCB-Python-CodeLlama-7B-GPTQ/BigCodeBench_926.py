import pandas as pd
import sqlite3
def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    """
    Loads data from an SQLite database into a Pandas DataFrame and performs a string replacement operation on a specified column.
    Specifically, replaces all occurrences of the newline character '\n' with the HTML line break tag '<br>'.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Query the database for the specified table and column
    query = f"SELECT * FROM {table_name} WHERE {column_name} LIKE '%\n%'"
    df = pd.read_sql(query, conn)

    # Replace the newline characters with the HTML line break tag
    df[column_name] = df[column_name].str.replace('\n', '<br>')

    # Close the connection to the database
    conn.close()

    return df
db_path = 'path/to/database.db'
table_name = 'table_name'
column_name = 'column_name'