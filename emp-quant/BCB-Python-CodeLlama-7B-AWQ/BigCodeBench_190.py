import sqlite3
import pandas as pd
import csv
from io import StringIO
DATABASE_NAME = 'test.db'
TABLE_NAME = 'test_table'
def task_func(csv_input):
    # Connect to the database
    conn = sqlite3.connect(DATABASE_NAME)
    # Create a new table or replace an existing one
    conn.execute('DROP TABLE IF EXISTS {}'.format(TABLE_NAME))
    conn.execute('CREATE TABLE {} (id INTEGER PRIMARY KEY, name TEXT, age INTEGER)'.format(TABLE_NAME))
    # Insert data into the table
    with open(csv_input, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            conn.execute('INSERT INTO {} VALUES (?, ?, ?)'.format(TABLE_NAME), row)
    # Query the table and return the data as a DataFrame
    df = pd.read_sql_query('SELECT * FROM {}'.format(TABLE_NAME), conn)
    return df