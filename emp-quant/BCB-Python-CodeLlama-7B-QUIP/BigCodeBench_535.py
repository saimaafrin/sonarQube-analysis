
import sqlite3
import numpy as np
from random import choice, seed

def task_func(db_path, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("num_entries cannot be negative")

    # Create the table if it doesn't exist
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS " + table_name + " (name TEXT, age INTEGER, height INTEGER)")

    # Insert random data into the table
    names = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    ages = np.random.randint(18, 64, num_entries)
    heights = np.random.randint(150, 199, num_entries)
    for i in range(num_entries):
        c.execute("INSERT INTO " + table_name + " (name, age, height) VALUES (?, ?, ?)", (names[i], ages[i], heights[i]))

    # Close the connection
    conn.close()

    return num_entries