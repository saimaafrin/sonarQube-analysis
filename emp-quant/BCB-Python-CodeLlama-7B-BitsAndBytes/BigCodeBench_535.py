
import sqlite3
import numpy as np
from random import choice, seed

def task_func(db_path, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("Number of entries must be non-negative")

    # Create the table if it does not exist
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS {} (name TEXT, age INTEGER, height REAL)".format(table_name))

    # Generate random data
    names = ['John', 'Jane', 'Steve', 'Emma', 'Liam', 'Olivia']
    ages = np.random.randint(18, 64, num_entries)
    heights = np.random.randint(150, 199, num_entries)

    # Insert the data into the table
    for i in range(num_entries):
        c.execute("INSERT INTO {} VALUES (?, ?, ?)".format(table_name), (names[i], ages[i], heights[i]))

    # Commit the changes and close the connection
    conn.commit()
    conn.close()

    return num_entries

print(task_func(db_path, table_name, num_entries, random_seed))