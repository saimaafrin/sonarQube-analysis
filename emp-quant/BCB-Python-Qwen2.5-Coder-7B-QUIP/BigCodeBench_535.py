
import sqlite3
import numpy as np
from random import choice, seed

def task_func(db_path, table_name, num_entries, random_seed=None):
    # Constants
    NAMES = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    AGES = range(18, 65)
    HEIGHTS = range(150, 200)

    # Validate num_entries
    if num_entries < 0:
        raise ValueError("num_entries must be non-negative")

    # Seed the random generator
    if random_seed is not None:
        seed(random_seed)

    # Connect to the SQLite database
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the table if it does not exist
    cursor.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, height INTEGER)")

    # Insert random data into the table
    inserted_rows = 0
    for _ in range(num_entries):
        name = choice(NAMES)
        age = np.random.choice(list(AGES))
        height = np.random.choice(list(HEIGHTS))
        cursor.execute(f"INSERT INTO {table_name} (name, age, height) VALUES (?, ?, ?)", (name, age, height))
        inserted_rows += 1

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    # Output the number of rows inserted
    return inserted_rows