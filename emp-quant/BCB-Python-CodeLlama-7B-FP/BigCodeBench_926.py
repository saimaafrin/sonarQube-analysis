import pandas as pd
import sqlite3
def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    """
    Load data from an SQLite database into a Pandas DataFrame and perform a string replacement operation on a specified column.
    Specifically, replaces all occurrences of the newline character '\n' with the HTML line break tag '<br>'.
    :param db_path: Path to the SQLite database file.
    :param table_name: Name of the table in the database.
    :param column_name: Name of the column in the table.
    :return: Modified Pandas DataFrame with replaced strings in the specified column.
    """
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)

    # Query the database and load the data into a Pandas DataFrame
    df = pd.read_sql_query(f"SELECT * FROM {table_name}", conn)

    # Replace all occurrences of the newline character '\n' with the HTML line break tag '<br>'
    df[column_name] = df[column_name].str.replace('\n', '<br>')

    # Close the SQLite connection
    conn.close()

    return df
db_path = 'path/to/database.db'
table_name = 'table_name'
column_name = 'column_name'