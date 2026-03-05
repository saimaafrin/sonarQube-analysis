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

    # Create a random seed if not provided
    if random_seed is None:
        random_seed = np.random.randint(1, 1000000)

    # Set the random seed
    np.random.seed(random_seed)

    # Create a list of possible names
    names = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']

    # Create a list of possible ages
    ages = np.arange(18, 65)

    # Create a list of possible heights
    heights = np.arange(150, 200)

    # Create a connection to the database
    conn = sqlite3.connect(db_path)

    # Create a cursor object
    c = conn.cursor()

    # Create the table if it does not exist
    c.execute("""
        CREATE TABLE IF NOT EXISTS {} (
            name TEXT,
            age INTEGER,
            height INTEGER
        )
    """.format(table_name))

    # Insert the data into the table
    for i in range(num_entries):
        c.execute("""
            INSERT INTO {} (name, age, height)
            VALUES (?, ?, ?)
        """.format(table_name), (
            choice(names),
            choice(ages),
            choice(heights)
        ))

    # Commit the changes
    conn.commit()

    # Close the cursor and the connection
    c.close()
    conn.close()

    # Return the number of rows inserted
    return c.rowcount