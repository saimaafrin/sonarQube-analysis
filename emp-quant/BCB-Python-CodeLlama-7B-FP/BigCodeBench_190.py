import sqlite3
import pandas as pd
import csv
from io import StringIO
DATABASE_NAME = 'test.db'
TABLE_NAME = 'test_table'
def task_func(csv_input):
    # Connect to the database
    conn = sqlite3.connect(DATABASE_NAME)
    c = conn.cursor()

    # Create a new table or replace an existing one
    c.execute(f'DROP TABLE IF EXISTS {TABLE_NAME}')
    c.execute(f'CREATE TABLE {TABLE_NAME} (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)')

    # Insert data into the table
    with open(csv_input, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # Skip the header row
        for row in reader:
            c.execute(f'INSERT INTO {TABLE_NAME} VALUES (?, ?, ?)', row)

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Query the table and return the data as a DataFrame
    df = pd.read_sql_query(f'SELECT * FROM {TABLE_NAME}', conn)
    return df
csv_input = 'data.csv'