import sqlite3
from random import choice, seed
import os
def task_func(db_name, table_name, num_entries, random_seed=None):
    """
    Creates an SQLite3 table and fills it with random data.

    Args:
        db_name (str): The name of the SQLite3 database file.
        table_name (str): The name of the table to be created.
        num_entries (int): The number of entries to be inserted into the table.
        random_seed (int, optional): The random seed to be used for generating random data.

    Returns:
        str: The absolute path of the SQLite3 database file.

    Raises:
        ValueError: If num_entries is negative.
    """
    if num_entries < 0:
        raise ValueError("num_entries must be non-negative")

    # Create the SQLite3 database file
    db_path = os.path.join(os.getcwd(), db_name)
    conn = sqlite3.connect(db_path)

    # Create the table
    cursor = conn.cursor()
    cursor.execute(f"CREATE TABLE {table_name} (name TEXT, age INTEGER, height INTEGER)")

    # Fill the table with random data
    names = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    ages = range(18, 65)
    heights = range(150, 200)

    for i in range(num_entries):
        name = choice(names)
        age = choice(ages)
        height = choice(heights)
        cursor.execute(f"INSERT INTO {table_name} VALUES ('{name}', {age}, {height})")

    # Commit the changes
    conn.commit()

    # Close the connection
    conn.close()

    return db_path
db_name = "test.db"
table_name = "test_table"
num_entries = 10
random_seed = 42