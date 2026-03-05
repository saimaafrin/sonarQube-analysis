import sqlite3
import pandas as pd
import csv
from io import StringIO
DATABASE_NAME = 'test.db'
TABLE_NAME = 'test_table'
def task_func(csv_input):
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(DATABASE_NAME)
    # Create a cursor object using the cursor() method
    cursor = conn.cursor()
    # Check if the table exists and drop it if it does
    cursor.execute(f"DROP TABLE IF EXISTS {TABLE_NAME}")
    # Create table as per requirement
    cursor.execute(f'''
        CREATE TABLE {TABLE_NAME} (
            id INTEGER PRIMARY KEY,
            name TEXT,
            age INTEGER,
            email TEXT
        )
    ''')
    # Check if the input is a file path or a StringIO object
    if isinstance(csv_input, str):
        # Open the CSV file
        with open(csv_input, mode='r', newline='') as file:
            csv_reader = csv.reader(file)
            # Skip the header row
            next(csv_reader)
            # Insert data into the table
            for row in csv_reader:
                cursor.execute(f'''
                    INSERT INTO {TABLE_NAME} (name, age, email)
                    VALUES (?, ?, ?)
                ''', (row[0], row[1], row[2]))
    elif isinstance(csv_input, StringIO):
        # Read the StringIO object
        csv_reader = csv.reader(csv_input.getvalue().splitlines())
        # Skip the header row
        next(csv_reader)
        # Insert data into the table
        for row in csv_reader:
            cursor.execute(f'''
                INSERT INTO {TABLE_NAME} (name, age, email)
                VALUES (?, ?, ?)
            ''', (row[0], row[1], row[2]))
    else:
        raise ValueError("Invalid input type. Expected a file path or a StringIO object.")
    # Commit the changes
    conn.commit()
    # Query the table to retrieve data
    cursor.execute(f"SELECT * FROM {TABLE_NAME}")
    # Fetch all rows from the last executed statement
    rows = cursor.fetchall()
    # Create a pandas DataFrame from the rows
    df = pd.DataFrame(rows, columns=['id', 'name', 'age', 'email'])
    # Close the database connection
    conn.close()
    # Return the DataFrame
    return df