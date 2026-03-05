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
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    matches = []
    for row in rows:
        if re.search(pattern, row[column_name]):
            matches.append(row)
    conn.close()
    return pd.DataFrame(matches)