import sqlite3
import numpy as np
from random import choice, seed
def task_func(db_path, table_name, num_entries, random_seed=None):
    """
    Insert random data into an SQLite3 table.

    Args:
        db_path (str): Path to the SQLite3 database file.
        table_name (str): Name of the table to insert data into.
        num_entries (int): Number of entries to insert.
        random_seed (int, optional): Random seed for reproducibility.

    Returns:
        int: Number of rows inserted.

    Raises:
        ValueError: If num_entries is negative.
    """
    if num_entries < 0:
        raise ValueError("Number of entries must be non-negative.")

    # Create the table if it does not exist
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute(f"CREATE TABLE IF NOT EXISTS {table_name} (name TEXT, age INTEGER, height INTEGER)")
    conn.commit()

    # Insert random data
    names = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    ages = np.random.randint(18, 64, size=num_entries)
    heights = np.random.randint(150, 199, size=num_entries)
    data = [(name, age, height) for name, age, height in zip(names, ages, heights)]
    c.executemany(f"INSERT INTO {table_name} VALUES (?, ?, ?)", data)
    conn.commit()

    # Return the number of rows inserted
    return c.execute(f"SELECT COUNT(*) FROM {table_name}").fetchone()[0]
db_path = "test.db"
table_name = "test_table"
num_entries = 10
random_seed = 42