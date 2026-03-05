import sqlite3
from random import choice, seed
import os
def task_func(db_name, table_name, num_entries, random_seed=None):
    # Check if num_entries is negative
    if num_entries < 0:
        raise ValueError("num_entries cannot be negative")
    
    # Define constants
    NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    AGES = range(18, 66)
    HEIGHTS = range(150, 201)
    
    # Set random seed if provided
    if random_seed is not None:
        seed(random_seed)
    
    # Create an absolute path for the database file
    db_path = os.path.abspath(db_name)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Create the table
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (name TEXT, age INTEGER, height INTEGER)")
    
    # Insert random data into the table
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(AGES)
        height = choice(HEIGHTS)
        cursor.execute(f"INSERT INTO {table_name} (name, age, height) VALUES (?, ?, ?)", (name, age, height))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    # Return the absolute path of the database file
    return db_path