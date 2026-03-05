
import sqlite3
import pandas as pd
import csv
from io import StringIO
# Constants
DATABASE_NAME = 'test.db'
TABLE_NAME = 'test_table'

def task_func(csv_input):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(DATABASE_NAME)
    
    # Create a cursor object using the cursor method
    cursor = conn.cursor()
    
    # Check if the table already exists and drop it if it does
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    
    # Create a new table
    cursor.execute(f"""
        CREATE TABLE {TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            column1 TEXT,
            column2 TEXT,
            column3 TEXT
        )
    """)
    
    # Check if the input is a file path or a StringIO object
    if isinstance(csv_input, str):
        # Read the CSV file
        with open(csv_input, 'r') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip the header row
            cursor.executemany(f"INSERT INTO {TABLE_NAME} VALUES (?, ?, ?)", csv_reader)
    elif isinstance(csv_input, StringIO):
        # Read the CSV from StringIO
        csv_reader = csv.reader(csv_input)
        next(csv_reader)  # Skip the header row
        cursor.executemany(f"INSERT INTO {TABLE_NAME} VALUES (?, ?, ?)", csv_reader)
    else:
        raise ValueError("csv_input must be a file path or a StringIO object")
    
    # Commit the changes
    conn.commit()
    
    # Query the table and load the data into a pandas DataFrame
    query = f"SELECT * FROM {TABLE_NAME}"
    df = pd.read_sql_query(query, conn)
    
    # Close the connection
    conn.close()
    
    return df