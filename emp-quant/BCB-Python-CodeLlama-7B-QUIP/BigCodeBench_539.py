
import sqlite3
from random import choice, seed
import os

def task_func(db_name, table_name, num_entries, random_seed=None):
    if num_entries < 0:
        raise ValueError("num_entries must be positive")

    # Create the database and table
    db_path = os.path.join(os.getcwd(), db_name)
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute("CREATE TABLE " + table_name + " (name TEXT, age INTEGER, height INTEGER)")

    # Populate the table with random data
    names = ["John", "Jane", "Steve", "Emma", "Liam", "Olivia"]
    ages = range(18, 65)
    heights = range(150, 200)
    for i in range(num_entries):
        c.execute("INSERT INTO " + table_name + " VALUES (?, ?, ?)", (choice(names), choice(ages), choice(heights)))

    # Close the connection
    conn.close()

    return db_path