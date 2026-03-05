import sqlite3
import pandas as pd
import os
def task_func(db_file, table_name, column_name, pattern='\d+[xX]'):
    """
    Find all matches with a regex pattern in a list of strings in an SQL database.
    The function loads an sql database and selects all entries from the specified table.
    Matches are returned in a DataFrame.
    """
    if not os.path.exists(db_file):
        raise ValueError("db_file does not exist")

    conn = sqlite3.connect(db_file)
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM {table_name} WHERE {column_name} REGEXP '{pattern}'")
    matches = cur.fetchall()
    conn.close()

    return pd.DataFrame(matches, columns=cur.description)
db_file = "example.db"
table_name = "example_table"
column_name = "example_column"
conn = sqlite3.connect(db_file)
cur = conn.cursor()
matches = cur.fetchall()
pattern = "12345"