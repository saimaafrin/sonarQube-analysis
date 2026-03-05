
import sqlite3
import pandas as pd
import os

def task_func(db_file, table_name, column_name, pattern='\d+[xX]'):
    if not os.path.exists(db_file):
        raise ValueError("DB file does not exist")
    conn = sqlite3.connect(db_file)
    with conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM " + table_name + " WHERE " + column_name + " LIKE " + pattern)
        result = cursor.fetchall()
    df = pd.DataFrame(result)
    return df