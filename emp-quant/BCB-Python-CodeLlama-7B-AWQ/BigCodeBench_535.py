import sqlite3
import numpy as np
from random import choice, seed
def task_func(db_path, table_name, num_entries, random_seed=None):
    """
    Insert random data into an SQLite3 table that contains random names, ages, and heights.
    If the table does not exist, it will be created.
    """
    if num_entries < 0:
        raise ValueError("num_entries must be non-negative")

    # Create a connection to the database
    conn = sqlite3.connect(db_path)

    # Create the table if it does not exist
    conn.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (name TEXT, age INTEGER, height INTEGER)")

    # Insert random data into the table
    for i in range(num_entries):
        name = choice(["John", "Jane", "Steve", "Emma", "Liam", "Olivia"])
        age = np.random.randint(18, 64)
        height = np.random.randint(150, 199)
        conn.execute(f"INSERT INTO {table_name} VALUES ('{name}', {age}, {height})")

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return num_entries