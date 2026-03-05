import pandas as pd
import sqlite3
def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    """
    Loads data from an SQLite database into a Pandas DataFrame and performs a string replacement operation on a specified column.
    Specifically, replaces all occurrences of the newline character '\n' with the HTML line break tag '<br>'.
    The function should output with:
        pd.DataFrame: The modified DataFrame with replaced strings in the specified column.
    """
    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Query the database
    query = f"SELECT * FROM {table_name}"
    df = pd.read_sql(query, conn)

    # Replace newline characters with HTML line breaks
    df[column_name] = df[column_name].str.replace('\n', '<br>')

    # Close the connection
    conn.close()

    return df