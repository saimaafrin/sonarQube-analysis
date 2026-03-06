
import sqlite3
from random import choice, seed
import os

def task_func(db_name, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("Number of entries must be non-negative")

    # Create the SQLite3 database and table
    db_path = os.path.join(os.getcwd(), db_name)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height REAL)")

    # Populate the table with random data
    names = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    ages = range(18, 65)
    heights = range(150, 200)
    for i in range(num_entries):
        name = choice(names)
        age = choice(ages)
        height = choice(heights)
        c.execute(f"INSERT INTO {table_name} VALUES ('{name}', {age}, {height})")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return db_path

try:
    db_path = task_func(db_name, table_name, num_entries, random_seed)
    print(f"Database path: {db_path}")
except ValueError as e:
    print(f"Error: {e}")