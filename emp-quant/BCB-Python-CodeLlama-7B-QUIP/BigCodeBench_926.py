
import pandas as pd
import sqlite3

def task_func(db_path: str, table_name: str, column_name: str) -> pd.DataFrame:
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    # Select the specified table
    table = conn.execute("SELECT * FROM " + table_name)
    # Convert the result to a Pandas DataFrame
    df = pd.DataFrame(table)
    # Replace the newline characters in the specified column with the HTML line break tag
    df[column_name] = df[column_name].str.replace('\n', '<br>')
    # Return the modified DataFrame
    return df