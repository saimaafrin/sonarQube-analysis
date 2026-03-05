import sqlite3
from random import choice, seed
import os
def task_func(db_name, table_name, num_entries, random_seed=None):
    """
    Create an SQLite3 table and fill it with random data using the provided database and table names.
    The function populates the table with columns 'name', 'age', 'height' using random data from the following constants:
    - NAMES: List of names ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    - AGES: Range of ages from 18 to 65.
    - HEIGHTS: Range of heights from 150cm to 200cm.
    The function should raise the exception for:
    ValueError: If num_entries is negative.
    The function should output with:
        str: The absolute path of the SQLite3 database file.
    """
    if num_entries < 0:
        raise ValueError("num_entries must be non-negative")

    # Create the database and table
    db_path = os.path.join(os.getcwd(), db_name)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height INTEGER)")

    # Populate the table with random data
    names = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    ages = range(18, 65)
    heights = range(150, 200)
    for i in range(num_entries):
        name = choice(names)
        age = choice(ages)
        height = choice(heights)
        c.execute(f"INSERT INTO {table_name} VALUES ('{name}', {age}, {height})")

    # Commit and close the connection
    conn.commit()
    conn.close()

    return db_path