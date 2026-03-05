import sqlite3
import pandas as pd
import csv
from io import StringIO
DATABASE_NAME = 'test.db'
TABLE_NAME = 'test_table'
def task_func(csv_input):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(DATABASE_NAME)
    
    # Create a cursor object using the cursor method
    cursor = conn.cursor()
    
    # Check if the table already exists and drop it if it does
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    
    # Create table
    cursor.execute(f'''
        CREATE TABLE {TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            column1 TEXT,
            column2 TEXT,
            column3 TEXT
        )
    ''')
    
    # Check if the input is a file path or StringIO
    if isinstance(csv_input, str):
        # Open the CSV file
        with open(csv_input, 'r') as file:
            csv_data = file.read()
    else:
        # Use the StringIO object directly
        csv_data = csv_input.getvalue()
    
    # Use pandas to read the CSV data
    df = pd.read_csv(StringIO(csv_data))
    
    # Insert data into the SQLite table
    for index, row in df.iterrows():
        cursor.execute(f'''
            INSERT INTO {TABLE_NAME} (column1, column2, column3)
            VALUES (?, ?, ?)
        ''', (row['column1'], row['column2'], row['column3']))
    
    # Commit the changes
    conn.commit()
    
    # Query the table to retrieve the data
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    rows = cursor.fetchall()
    
    # Create a new DataFrame from the query results
    result_df = pd.DataFrame(rows, columns=[description[0] for description in cursor.description])
    
    # Close the connection
    conn.close()
    
    return result_df