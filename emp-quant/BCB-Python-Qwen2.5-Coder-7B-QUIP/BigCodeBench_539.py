
import sqlite3
from random import choice, seed
import os

def task_func(db_name, table_name, num_entries, random_seed=None):
    # Validate num_entries
    if num_entries < 0:
        raise ValueError("num_entries must be non-negative")

    # Define the constants
    NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    AGES = range(18, 66)
    HEIGHTS = range(150, 201)

    # Ensure the database file exists
    if not os.path.exists(db_name):
        raise FileNotFoundError(f"Database file {db_name} not found")

    # Connect to the SQLite3 database
    conn = sqlite3.connect(db_name)
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (name TEXT, age INTEGER, height INTEGER)")

    # Seed the random generator if a seed is provided
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

    # Return the absolute path of the database file
    return os.path.abspath(db_name)