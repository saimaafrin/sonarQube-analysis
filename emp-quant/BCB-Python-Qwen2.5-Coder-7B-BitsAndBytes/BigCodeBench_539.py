
import sqlite3
from random import choice, seed
import os

NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
AGES = range(18, 66)
HEIGHTS = range(150, 201)

def task_func(db_name, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("num_entries cannot be negative")
    
    # Ensure the directory exists
    db_dir = os.path.dirname(db_name)
    if not os.path.exists(db_dir):
        os.makedirs(db_dir)
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()
    
    # Create the table
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, age INTEGER, height INTEGER)")
    
    # Seed the random number generator if a seed is provided
    if random_seed is not None:
        seed(random_seed)
    
    # Insert random data into the table
    for _ in range(num_entries):
        name = choice(NAMES)
        age = choice(list(AGES))
        height = choice(list(HEIGHTS))
        cursor.execute(f"INSERT INTO {table_name} (name, age, height) VALUES (?, ?, ?)", (name, age, height))
    
    # Commit the changes and close the connection
    conn.commit()
    conn.close()
    
    return os.path.abspath(db_name)