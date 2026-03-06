import sqlite3
import numpy as np
from random import choice, seed
def task_func(db_path, table_name, num_entries, random_seed=None):
    """
    Insert random data into an SQLite3 table that contains random names, ages, and heights.
    If the table does not exist, it will be created.
    This function uses the following constants:
    - NAMES: List of possible names ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia'].
    - AGES: Range of possible ages from 18 to 64.
    - HEIGHTS: Range of possible heights from 150cm to 199cm.

    Parameters:
    db_path (str): The path to the SQLite3 database file.
    table_name (str): The name of the table to insert data into.
    num_entries (int): The number of entries to insert. Must not be negative.
    random_seed (int, optional): Seed for random number generation. Defaults to None (no fixed seed).

    Returns:
    int: The number of rows inserted.

    Raises:
    ValueError: If num_entries is negative.
    
    Requirements:
    - sqlite3
    - numpy
    - random.choice
    - random.seed

    Example:
    >>> task_func('path_to_test.db', 'People', 100, random_seed=42)
    100
    """
    if num_entries < 0:
        raise ValueError('num_entries must be non-negative')

    # Connect to the database
    conn = sqlite3.connect(db_path)

    # Create the table if it does not exist
    conn.execute('CREATE TABLE IF NOT EXISTS {} (name TEXT, age INT, height INT)'.format(table_name))

    # Insert random data into the table
    names = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    ages = range(18, 65)
    heights = range(150, 200)
    if random_seed is not None:
        seed(random_seed)
    for _ in range(num_entries):
        conn.execute('INSERT INTO {} VALUES (?, ?, ?)'.format(table_name), (choice(names), choice(ages), choice(heights)))

    # Close the connection
    conn.close()

    # Return the number of rows inserted
    return num_entries