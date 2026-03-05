
import sqlite3
import pandas as pd
import csv
from io import StringIO
# Constants
DATABASE_NAME = 'test.db'
TABLE_NAME = 'test_table'

def task_func(csv_input):
    # Create a new database table or replace an existing one
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()
    c.execute("DROP TABLE IF EXISTS " + TABLE_NAME)
    c.execute("CREATE TABLE " + TABLE_NAME + " (id INTEGER PRIMARY KEY, name TEXT)")
    conn.commit()

    # Insert data into the table
    with open(csv_input, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            c.execute("INSERT INTO " + TABLE_NAME + " VALUES (?, ?)", (row[0], row[1]))
    conn.commit()

    # Query the table and return the data as a DataFrame
    c.execute("SELECT * FROM " + TABLE_NAME)
    result = c.fetchall()
    conn.close()
    return pd.DataFrame(result, columns=['id', 'name'])