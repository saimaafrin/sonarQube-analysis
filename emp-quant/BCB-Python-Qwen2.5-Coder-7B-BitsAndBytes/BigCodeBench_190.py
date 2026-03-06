
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
    
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()
    
    # Check if the table already exists and drop it if it does
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    
    # Create table as per requirement
    cursor.execute(f'''
        CREATE TABLE {TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER NOT NULL,
            email TEXT NOT NULL
        )
    ''')
    
    # Insert data into the table
    if isinstance(csv_input, str):
        # Read CSV file from file path
        with open(csv_input, mode='r') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header row
            cursor.executemany(f'INSERT INTO {TABLE_NAME} VALUES (?, ?, ?, ?)', reader)
    elif isinstance(csv_input, StringIO):
        # Read CSV data from StringIO
        reader = csv.reader(csv_input.getvalue().splitlines())
        next(reader)  # Skip header row
        cursor.executemany(f'INSERT INTO {TABLE_NAME} VALUES (?, ?, ?, ?)', reader)
    else:
        raise ValueError("csv_input must be either a string file path or a StringIO object")
    
    # Commit the changes
    conn.commit()
    
    # Query the table to retrieve all rows
    cursor.execute(f'SELECT * FROM {TABLE_NAME}')
    rows = cursor.fetchall()
    
    # Get column names
    columns = [description[0] for description in cursor.description]
    
    # Close the connection
    conn.close()
    
    # Convert the list of tuples to a pandas DataFrame
    df = pd.DataFrame(rows, columns=columns)
    
    return df